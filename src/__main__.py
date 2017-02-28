#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Main entry point of the software. Chooses the algorithm to apply and the inputs
and outputs
"""
# Libraries
import os
import sys
import platform
import logging
import core.log

from cli.arguments.parser import DEFAULT_PARSER
from cli.arguments.word_count import WORD_COUNT_PARSER
from cli.arguments.constants import LOGS_LEVELS, LOGS, LOG_DEFAULT,\
                                    TASK_DEFAULT

# Constants
LOGGER = None

# Variables
"""
Arguments namespace
"""
args = None


# Functions
def parse_arguments(parser, args=None):
    """
    Given an argument parser and arguments as a list, parses the arguments and
    returns the parsed arguments

    Args:
        parser (ArgumentParser): argument parser to use with the args
        args (list): list of string arguments
    Returns:
        namespace: arguments namespace
    """
    return parser.parse_known_args(args)[0]


if __name__ == "__main__":
    # Prepare coding
    if platform.system() == "Windows":
        os.system("chcp 65001")
    # Load arguments
    args = parse_arguments(DEFAULT_PARSER)
    # Init logging
    core.log.init()
    LOGGER = logging.getLogger(__name__)

    # Set task and log_level
    task = args.task
    log_level = args.log_level

    # No task specified
    if task is None:
        # Check if help is wanted
        if args.help:
            DEFAULT_PARSER.print_help()
            sys.exit(0)
        # Task is default
        task = TASK_DEFAULT
    # Switch task and parse
    if task == "word-count":
        args = parse_arguments(WORD_COUNT_PARSER)
    elif task == "letter-count":
        LOGGER.error("Not implemented yet")
        sys.exit(1)
    else:
        LOGGER.error("No valid task has been selected, check usage")
        sys.exit(1)

    # Welcome
    LOGGER.info("Welcome to map-reduce testing")
    root_logger = logging.getLogger()

    # Change log level
    if log_level != LOG_DEFAULT:
        root_logger.setLevel(LOGS_LEVELS[LOGS.index(log_level)])
        LOGGER.info("Changed log level to %s", log_level)

    # Exiting
    LOGGER.info("Good bye!")
