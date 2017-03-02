"""
Defines the CLI controller for the task of using map-reduce to count items
in a text
"""
# Libraries
from .controller import controller
from .parser import create_full_parser

__all__ = ["controller", "create_full_parser"]
