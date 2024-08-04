import pytest
import subprocess
import sys
import os
import platform
import string
from collections import Counter
from zsk4gm.process_text import clean_text, tokenize, count_words

sys.path.insert(0, 'src')


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
    result = subprocess.run(["make", "-f", makefile_path, "get_texts"], capture_output=True, text=True)
    
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)
    
    if result.returncode != 0:
        pytest.fail(f"Makefile command failed with error:\n{result.stderr}")

    def cleanup_books_directory():
        try:
            subprocess.run(["rm", "-rf", "books"], check=True)
            print("Removed 'books' directory after tests")
        except subprocess.CalledProcessError as e:
            print(f"Failed to remove 'books' directory: {e}")
    
    request.addfinalizer(cleanup_books_directory)


@pytest.fixture
def raven_text(fetch_texts):
    with open('books/pg17192.txt', 'r', encoding='utf-8') as file:
        return file.read()


@pytest.fixture
def read_file():
    def _read_file(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    return _read_file


ENGLISH_FILES = [
    "books/pg17192.txt",
    "books/pg932.txt",
    "books/pg1063.txt",
    "books/pg10031.txt",
]


@pytest.fixture
def combined_text():
    combined = ""
    for filename in ENGLISH_FILES:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
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


def test_counter(sample_text):
    counts = count_words(sample_text)
    assert counts == {'but': 1, 'the': 2, 'raven': 1, 'sitting': 1, 'lonely': 1, 'on': 1, 'placid': 1,
                      'bust': 1, 'spoke': 1, 'only': 1, 'that': 2, 'one': 2, 'word': 2, 'as': 1, 'if': 1,
                      'his': 1, 'soul': 1, 'in': 1, 'he': 1, 'did': 1, 'outpour': 1}
    assert isinstance(counts, dict), "Tokenizer output is the incorrect dtype"
    assert counts == Counter(tokenize(sample_text))


@expected_to_fail
def test_counter_intended_failure_type():
    with pytest.raises(AssertionError):
        Counter(123)


def test_counter_raven(raven_text):
    counts = count_words(raven_text)
    assert isinstance(counts, dict), "Tokenizer output is the incorrect dtype"
    assert counts == Counter(tokenize(raven_text))


@pytest.mark.parametrize("filename", ENGLISH_FILES)
def test_counter_english_files(filename, read_file):
    file_content = read_file(filename)
    counts = count_words(file_content)
    assert isinstance(counts, dict), "Tokenizer output is the incorrect dtype"
    assert counts == Counter(tokenize(file_content))


def test_counter_combined(combined_text):
    counts = count_words(combined_text)
    assert isinstance(counts, dict), "Tokenizer output is the incorrect dtype"
    assert counts == Counter(tokenize(combined_text))


def test_counter_french(french_text):
    counts = count_words(french_text)
    assert isinstance(counts, dict), "Tokenizer output is the incorrect dtype"
    assert counts == Counter(tokenize(french_text))


@pytest.mark.skip(reason="Japanese version is not ready yet")
def test_counter_japanese():
    japanese_text = "insert Japanese text here"
    counts = count_words(japanese_text)
    assert isinstance(counts, dict), "Tokenizer output is the incorrect dtype"
    assert counts == Counter(tokenize(japanese_text))


def test_os_supported():
    supported_os = ["Linux"]
    current_os = platform.system()
    if current_os not in supported_os:
        pytest.fail(f"Tests have not been verified on the current OS: {current_os}")
    else:
        assert True


def test_python_version():
    min_version = (3, 7)
    max_version = (3, 12)
    current_version = sys.version_info[:2]
    if not (min_version <= current_version <= max_version):
        pytest.fail(f"Tests have not been verified on the current Python version: {current_version}. Supported versions are from {min_version} to {max_version}.")
    else:
        assert True


def test_clean_text_with_bash(sample_text):
    expected_counts = count_words(sample_text)

    bash_command = f"echo \"{sample_text}\" | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr ' ' '\\n' | sort | uniq -c"
    result = subprocess.run(bash_command, shell=True, capture_output=True, text=True, check=True)
    bash_output = result.stdout.strip()

    bash_counts = Counter()
    for line in bash_output.split('\n'):
        count, word = line.strip().split()
        bash_counts[word] = int(count)
    
    assert expected_counts == bash_counts, f"Bash result: {bash_counts} != Function result: {expected_counts}"
