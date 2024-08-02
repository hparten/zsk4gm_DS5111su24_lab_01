"""
This module contains integration tests for the zsk4gm.process_text functions.
"""

import os
import sys
from collections import Counter

import pytest

sys.path.insert(0, 'src')
from zsk4gm.process_text import clean_text, tokenize, count_words

# Determine the root directory of your project
root_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the log file relative to the root directory
log_file_path = os.path.join(root_dir, 'logs', 'test_logfile.log')

@pytest.mark.integration
def test_integration():
    """Integration test for clean_text, tokenize, and count_words functions."""
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
    """Test edge cases for clean_text, tokenize, and count_words functions."""
    assert clean_text(input_text) == expected_clean
    assert tokenize(input_text) == expected_tokens
    assert count_words(input_text) == expected_counts

@pytest.mark.integration
def test_failing_case():
    """Purposefully failing test case."""
    input_text = "This test should fail"
    expected_clean = "this test should pass"
    expected_tokens = ["this", "test", "should", "fail"]
    expected_counts = Counter({"this": 1, "test": 1, "should": 1, "fail": 1})

    cleaned_text = clean_text(input_text)
    assert cleaned_text == expected_clean, (
        f"Expected clean_text to be '{expected_clean}', but got '{cleaned_text}'"
    )
    tokens = tokenize(input_text)
    assert tokens == expected_tokens, (
        f"Expected tokens to be '{expected_tokens}', but got '{tokens}'"
    )
    word_counts = count_words(input_text)
    assert word_counts == expected_counts, (
        f"Expected word counts to be '{expected_counts}', but got '{word_counts}'"
    )
