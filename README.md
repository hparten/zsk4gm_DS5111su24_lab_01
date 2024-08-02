# zsk4gm_DS5111su24_lab_01

### process_text.py
This python module contain functions to process textual input

1. `clean_text(text)` lowercases and removes punctuation from input string
  - clean_text('Hi it is so nice to meet you!') -> 'hi it is so nice to meet you'
2. `tokenize(text)` splits the output from clean_text function for the input string
  - tokenize('Hi it is so nice to meet you!') -> ['hi', 'it', 'is', 'so', 'nice', 'to', 'meet', 'you']
3. `count_words(text)` counts the instances of each unique token from tokenize function for the input string.
  - counter_words('Hi it is so nice to meet you!') -> {'hi':1, 'it':1, 'is':1, 'so':1, 'nice':1, 'to':2, 'meet':1, 'you':1}
