#!/usr/bin/env python

from collections import Counter
import sys


def main():
    try:
        phrases = " ".join(sys.argv[1:])
        if not phrases:
            raise IndexError
        phrases = [phrases]
    except IndexError:
        print "Reading..."
        with open('./phrases.txt', 'r') as f:
            phrases = list(f.readlines())
    valid = 0
    for p in phrases:
        if is_extra_valid(p):
            valid += 1

    print valid


def is_valid(phrase):
    c = Counter(phrase.split())
    if any(w > 1 for w in c.values()):
        return False
    return True


def is_extra_valid(phrase):
    print phrase
    words = [Counter(w.strip()) for w in phrase.split()]
    for i in range(len(words) - 1):
        print words
        print i
        check = words.pop()
        if check in words:
            return False

    return True


if __name__ == '__main__':
    main()
