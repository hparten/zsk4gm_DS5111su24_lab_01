import pytest
import subprocess
import sys
import os
sys.path.insert(0, 'src')  
from zsk4gm.process_text import clean_text, tokenize
import platform
import string

@pytest.fixture
def sample_text():
    return "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."


# Custom decorator
def expected_to_fail(func):
    func = pytest.mark.xfail(func)
    return func


@pytest.fixture(scope="session", autouse=True)
def fetch_texts(request):
    makefile_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'makefile')
    # Run the 'make get_texts' command
    result = subprocess.run(["make", "-f", makefile_path, "get_texts"], capture_output=True, text=True)
        
    # Print stdout and stderr for debugging
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)
    
    if result.returncode != 0:
        pytest.fail(f"Makefile command failed with error:\n{result.stderr}")

    # Define cleanup function to remove books directory
    def cleanup_books_directory():
        try:
            subprocess.run(["rm", "-rf", "books"], check=True)
            print("Removed 'books' directory after tests")
        except subprocess.CalledProcessError as e:
            print(f"Failed to remove 'books' directory: {e}")
    
    # Register cleanup function as a finalizer
    request.addfinalizer(cleanup_books_directory)



@pytest.fixture
def raven_text(fetch_texts):
    with open('books/pg17192.txt', 'r') as file:
        return file.read()

# Custom fixture
@pytest.fixture
def read_file():
    def _read_file(filename):
        with open(filename, 'r') as file:
            return file.read()
    return _read_file


ENGLISH_FILES = [
        "books/pg17192.txt",  # The Raven
        "books/pg932.txt",    # Fall of the House of Usher
        "books/pg1063.txt",   # Cask of Amontiallado
        "books/pg10031.txt",  # The Poems
]

@pytest.fixture
def combined_text():
    combined = ""
    for filename in ENGLISH_FILES:
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                combined += file.read() + " "
    return combined.strip()


@pytest.fixture
def french_text():
    return ("Mais le Corbeau, perché solitairement sur ce buste placide, parla "
            "ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne "
            "proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce "
            "que je fis à peine davantage que marmotter «D'autres amis déjà ont "
            "pris leur vol--demain il me laissera comme mes Espérances déjà ont "
            "pris leur vol.» Alors l'oiseau dit: «Jamais plus.»")


# Test of the sample English text
def test_tokenizer(sample_text):
    # Given a text string
    # When the text is tokenized
    tokens = tokenize(sample_text)
    # Then the tokens should be same words in a lowercase list without punctuation
    assert tokens == ['but','the', 'raven', 'sitting', 'lonely', 'on', 'the', 'placid',
		      'bust', 'spoke', 'only', 'that', 'one', 'word', 'as', 'if', 'his', 'soul',
		      'in', 'that', 'one', 'word', 'he', 'did', 'outpour']
    assert isinstance(tokens, list), f"Tokenizer output is the incorrect dtype"
    assert tokens == clean_text(sample_text).split()



# Test of the input type that is expected to fail
@expected_to_fail
def test_tokenizer_intended_failure_type():
    # Given an integer instead of a string
    # When the text is cleaned
    # Then an assertion error should be raised
    with pytest.raises(AssertionError):
        tokenize(123)


# Test to check function on just the Raven
def test_clean_text_raven(raven_text):
    # Given a text string
    # When the text is tokenized
    tokens = tokenize(raven_text)
    # Then the tokens should be same words in a lowercase list without punctuation
    assert isinstance(tokens, list), f"Tokenizer output is the incorrect dtype"
    assert tokens == clean_text(raven_text).split()


# Test to check function on each English text separately
@pytest.mark.parametrize("filename", ENGLISH_FILES)
def test_clean_text_english_files(filename, read_file):
    # Given the text from a file
    tokens = tokenize(filename)
    # Then the tokens should be same words in a lowercase list without punctuation
    assert isinstance(tokens, list), f"Tokenizer output is the incorrect dtype"
    assert tokens == clean_text(filename).split()


# Test to check function on all English texts combined
def test_clean_text_combined(combined_text):
    # Given a text string
    # When the text is tokenized
    tokens = tokenize(combined_text)
    # Then the tokens should be same words in a lowercase list without punctuation
    assert isinstance(tokens, list), f"Tokenizer output is the incorrect dtype"
    assert tokens == clean_text(combined_text).split()


# Test to check function on Le Corbeau text
def test_clean_text_french(french_text):
    # Given a text string
    # When the text is tokenized
    tokens = tokenize(french_text)
    # Then the tokens should be same words in a lowercase list without punctuation
    assert isinstance(tokens, list), f"Tokenizer output is the incorrect dtype"
    assert tokens == clean_text(french_text).split()

# Test for future Japanese version, marked to be skipped
@pytest.mark.skip(reason="Japanese version is not ready yet")
def test_clean_text_japanese():
    # Given a Japanese text
    japanese_text = "insert Japanese text here"
    # When the text is cleaned
    tokens = tokenize(japanese_text)
    # Then the tokens should be same words in a lowercase list without punctuation
    assert isinstance(tokens, list), f"Tokenizer output is the incorrect dtype"
    assert tokens == clean_text(japanese_text).split()

# Test to check if the OS is supported
def test_os():
    # Given the list of supported os and the current os
    supported_os = ["Linux"]
    current_os = platform.system()
    # When compared
    # Then the current os should be in the list of supported os
    if current_os not in supported_os:
        pytest.fail(f"Tests have not been verified on the current OS: {current_os}")
    else:
        assert True


# Test to check if the Python version is supported
def test_python_version():
    # Given the minimum and maximum supported Python versions and current version
    min_version = (3, 7)
    max_version = (3, 12)
    current_version = sys.version_info[:2]
    # When versions are compared
    # The the supported version fall within the min and max version
    if not (min_version <= current_version <= max_version):
        pytest.fail(f"Tests have not been verified on the current Python version: {current_version}. Supported versions are from {min_version} to {max_version}.")
    else:
        assert True


# Test to compare function against bash command
def test_clean_text_with_bash(sample_text):
    # Given a cleaned text string  using function
    expected_tokens = tokenize(sample_text)

    # When a Bash command is used to tokenize the text string
    bash_command = f"echo \"{sample_text}\" | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | awk '{{for(i=1;i<=NF;i++) print $i}}'"
    result = subprocess.run(bash_command, shell=True, capture_output=True, text=True)
    bash_tokens = result.stdout.strip().split('\n')

    # Then the two cleaned text strings should be the same
    assert expected_tokens == bash_tokens, f"Bash result: {bash_cleaned} != Function result: {expected_cleaned}"
  
