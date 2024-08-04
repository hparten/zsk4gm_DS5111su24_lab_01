"""Module for text processing operations."""
import string
import logging
from collections import Counter
import os

root_dir = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(root_dir, 'logs', 'logfile.log')
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s',
                    filename=log_file_path)

def clean_text(text):
    """Clean the input text by removing punctuation and converting to lowercase."""
    assert isinstance(text, str), 'Input must be a string'
    logging.debug('Cleaning text: %s', text)
    text = text.lower()
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
    assert isinstance(cleaned_text, str), 'Output must be a string'
    logging.debug('Cleaned text: %s', cleaned_text)
    return cleaned_text or ""

def tokenize(text):
    """Tokenize the input text into words."""
    assert isinstance(text, str), 'Input must be a string'
    logging.debug('Tokenizing text: %s', text)
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    assert isinstance(words, list), 'Output must be a list'
    assert all(isinstance(word, str) for word in words), 'All words in list must be strings'
    logging.debug('Tokenized words: %s', words)
    return words

def count_words(text):
    """Count the occurrence of each word in the input text."""
    assert isinstance(text, str), 'Input must be a string'
    logging.debug('Counting words in text %s', text)
    tokens = tokenize(text)
    word_count = Counter(tokens)
    assert isinstance(word_count, dict), 'Output must be a dict'
    assert all(isinstance(word, str) for word in word_count.keys()), 'All keys must be str'
    assert all(isinstance(count, int) for count in word_count.values()), 'All counts must be int'
    logging.debug('Counts for each word: %s', word_count)
    return word_count
