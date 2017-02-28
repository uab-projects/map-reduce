"""
Defines the CLI controller for the task of using map-reduce to count items
in a text
"""
# Libraries
from .parser import PARSER
from .workflow import controller

__all__ = ["PARSER", "controller"]
