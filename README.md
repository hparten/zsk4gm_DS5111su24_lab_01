[![Python package](https://github.com/hparten/zsk4gm_DS5111su24_lab_01/actions/workflows/validations.yml/badge.svg)](https://github.com/hparten/zsk4gm_DS5111su24_lab_01/actions/workflows/validations.yml)
# zsk4gm_DS5111su24_lab_01

### Installation 
You can install `zsk4gm` directly from GitHub using `git+http`:

```bash
pip install git+http://github.com/hparten/zsk4gm_DS5111su24_lab_01@WEEK-06/installable_package

### Example
Here's a quick example of how to use `zsk4gm`:
```

```python
import zsk4gm as pkg

test_string = "Hello world, this is a test"

print(pkg.clean_text(test_string)) 
print(pkg.tokenize(test_string)) 
print(pkg.count_words(test_string)) -> 
```

### zsk4gm
This python module contain functions to process textual input

1. `clean_text(text)` lowercases and removes punctuation from input string
  - clean_text('Hi it is so nice to meet you!') -> 'hi it is so nice to meet you'
2. `tokenize(text)` splits the output from clean_text function for the input string
  - tokenize('Hi it is so nice to meet you!') -> ['hi', 'it', 'is', 'so', 'nice', 'to', 'meet', 'you']
3. `count_words(text)` counts the instances of each unique token from tokenize function for the input string.
  - counter_words('Hi it is so nice to meet you!') -> {'hi':1, 'it':1, 'is':1, 'so':1, 'nice':1, 'to':2, 'meet':1, 'you':1}
