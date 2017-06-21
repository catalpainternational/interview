#!/usr/bin/env python

import collections


def count_words_by_first_letter(words):
    """ Takes a sequence of words and prints the number of words that start with
    each letter a-through-z.

    For example, the input ["alpha, "Apple", "zebra", "gamma"] should yield the
    following output:

      a: 2
      g: 1
      z: 1

    Args:
      words: A sequence of strings
    """
    assert isinstance(words, collections.Sequence)
