import pytest
from collections import Counter
import subprocess
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from process_text import clean_text, tokenize, count_words

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
