from collections import Counter


def is_isogram(string):
    return len(string) == 0 or Counter(string.replace('-', '').replace(' ', '').lower()).most_common(n=1)[0][1] <= 1
