def test_tokenize():
    # Given a string _text_ of text with words
    # When I pass _text_ to the `tokenize()` function
    # I should get an int as return representing the number of blocks of continuous text in the string

    text = 'philosophical prose poem of "Eureka," which he deemed the crowning work'

    assert isinstance(tokenize(text), list), f"Tokenizer failed on sample text: {text}"
