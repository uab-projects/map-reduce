"""
Defines argument parsers for the CLI interfaces, using the Python argparse
library
"""
import argparse
import ast
from .constants import LOGS, LOG_DEFAULT, TASKS, TASK_DEFAULT


# Auxiliary methods
def evalTF(string):
    """
    Converts a string to uppercase + lowercase letters to be able to determine
    if the string means true or false, so any case independent string
    containing true or false will be converted to their bool values

    Args:
        string (str): string to see if means true or false
    Returns:
        bool: true if string means true, false otherwise
    Raises:
        Exception: if string can't be determined as true or false
    """
    return ast.literal_eval(string.title())


# Default parser generator
def create_parser():
    """
    Creates an argument parser for the controller and returns it

    Returns:
        ArgumentParser: controller argument parser
    """
    parser = argparse.ArgumentParser(
        # prog = ''
        # usage = (generated by default)
        description="""Implements the map-reduce paradigm using multiple
        processes and allows to define user-defined tasks to apply to these
        paradigm to.
        Currently the only defined tasks are for text word and letter
        counting""",
        epilog="<> with ♥ by @ccebrecos and @davidlj95 at ETSE UAB, Spain",
        add_help=False
    )
    return parser


def create_parser_options(parser):
    """
    Given a parser, adds required arguments to it by the controller and returns
    the parser

    Args:
        ArgumentParser: argument parser to fill
    Returns:
        ArgumentParser: filled argument parser
    """
    parser.add_argument(
        "-v", "--version",
        action="version",
        version="map-reduce tester 1.0"
    )
    parser.add_argument(
        "-h", "--help",
        action="store_true",
        help="""show this help message and exit. If a task is specified,
        shows the task's help and exits""",
        default=False
    )
    parser.add_argument(
        "-l", "--log-level",
        metavar="level",
        action="store",
        help="""specifies the level of events to log. Events upper from that
        level will be displayed. Default is %s""" % (LOG_DEFAULT),
        type=str,
        choices=LOGS,
        default=LOG_DEFAULT
    )

    # Map - Reduce tasks
    parser.add_argument(
        "-t", "--task",
        metavar="task",
        action="store",
        help="""specifies the task to perform using map - reduce paradigm.
        Available tasks are %s. Default is %s""" % (TASKS, TASK_DEFAULT),
        type=str,
        choices=TASKS,
        default=None
    )

    return parser