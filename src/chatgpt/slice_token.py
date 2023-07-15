from nltk.tokenize import word_tokenize
from itertools import islice

def cut_tokens(text, max_tokens=2000):
    tokens = word_tokenize(text)
    if len(tokens) > max_tokens:
        tokens = list(islice(tokens, max_tokens))
    return ' '.join(tokens)