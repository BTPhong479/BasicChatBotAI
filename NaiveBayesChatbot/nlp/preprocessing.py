import re

def tokenize(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]","",text)
    tokens = text.split()

    return tokens