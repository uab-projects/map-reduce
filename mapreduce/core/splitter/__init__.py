"""
This module contains classes to perform the first step on every map-reduce
paradigm software: split the problem to deal with.

We've implemented just splitters that read from disk text (utf-8) files and
ables them to send it to a pool (a map pool in most cases)
"""
from .letterfile import LetterFileSplitter
from .wordfile import WordFileSplitter

__all__ = ["WordFileSplitter", "LetterFileSplitter"]
