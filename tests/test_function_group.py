import pytest
from collections import Counter
import subprocess
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from process_text import clean_text, tokenize, count_words
import logging

# Determine the root directory of your project
root_dir = os.path.dirname(os.path.abspath(__file__))  # This gets the directory of the current script
# Construct the path to the log file relative to the root directory
log_file_path = os.path.join(root_dir, 'logs', 'test_logfile.log')


@pytest.mark.integration
def test_integration():
    # Test input
    input_text = "Hello, World! This is a test. Hello again."

    # Test clean_text
    cleaned_text = clean_text(input_text)
    assert cleaned_text == "hello world this is a test hello again"

    # Test tokenize
    tokens = tokenize(input_text)
    assert tokens == ["hello", "world", "this", "is", "a", "test", "hello", "again"]

    # Test count_words
    word_counts = count_words(input_text)
    expected_counts = Counter({"hello": 2, "world": 1, "this": 1, "is": 1, "a": 1, "test": 1, "again": 1})
    assert word_counts == expected_counts

@pytest.mark.integration
@pytest.mark.parametrize("input_text, expected_clean, expected_tokens, expected_counts", [
    ("", "", [], {}),
    ("!@#$%^&*()", "", [], {}),
    ("HELLO hello HeLLo world WORLD", 
     "hello hello hello world world",
     ["hello", "hello", "hello", "world", "world"],
     {"hello": 3, "world": 2})
])
def test_edge_cases(input_text, expected_clean, expected_tokens, expected_counts):
    assert clean_text(input_text) == expected_clean
    assert tokenize(input_text) == expected_tokens
    assert count_words(input_text) == expected_counts

# Purposefully failing test
@pytest.mark.integration
def test_failing_case():
    input_text = "This test should fail"
    expected_clean = "this test should pass" 
    expected_tokens = ["this", "test", "should", "fail"]
    expected_counts = Counter({"this": 1, "test": 1, "should": 1, "fail": 1})
    
    cleaned_text = clean_text(input_text)
    assert cleaned_text == expected_clean, f"Expected clean_text to be '{expected_clean}', but got '{cleaned_text}'"

    tokens = tokenize(input_text)
    assert tokens == expected_tokens, f"Expected tokens to be '{expected_tokens}', but got '{tokens}'"

    word_counts = count_words(input_text)
    assert word_counts == expected_counts, f"Expected word counts to be '{expected_counts}', but got '{word_counts}'"

# Additional step to cat the logs if a test fails
def pytest_runtest_makereport(item, call):
    if call.excinfo is not None:
        # This runs only if the test fails
        if os.path.exists(log_file_path):
            with open(log_file_path, 'r') as log_file:
                logs = log_file.read()
                print(f"\n\nLOGS:\n{logs}\n\n")
