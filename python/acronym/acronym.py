import string


def abbreviate(words):
    words = words.replace("-")
    for punc in string.punctuation:
        words = words.replace(punc, "")
    return "".join([word[0].upper() for word in words.split()])
