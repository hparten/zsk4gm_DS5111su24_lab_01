import string
import logging
from collections import Counter

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')


def clean_text(text):
	assert isinstance(text, str)
	logging.debug(f'Cleaning text: {text}'), 'Input must be a string' 

	text = text.lower()
	cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
	
	assert isinstance(cleaned_text, str), 'Output must be a string'
	assert cleaned_text, 'Check output text is not None'
	logging.debug(f'Cleaned text: {cleaned_text}')
	
	return cleaned_text

def tokenize(text):
	assert isinstance(text, str), 'Input must be a string'
	logging.debug(f'Tokenizing text: {text}')
	
	cleaned_text = clean_text(text)
	words = cleaned_text.split()
	
	assert isinstance(words, list), 'Output must be a list'	
	assert all(isinstance(word, str) for word in words), 'All words in list must be strings' 
	logging.debug(f'Tokenized words: {words}')
	
	return words

def count_words(text):
    assert isinstance(text, str), 'Input must be a string'
    logging.debug(f'Counting words in text {text}')

    tokens = tokenize(text)

    word_count = Counter(tokens)

    assert isinstance(word_count, dict), 'Output must be a dict'
    assert all(isinstance(word, str) for word in word_count.keys()), 'All keys must be str'
    assert all(isinstance(count, int) for count in word_count.values()), 'All counts must be int'
    logging.debug(f'Counts for each word: {word_count}')

    return word_count


