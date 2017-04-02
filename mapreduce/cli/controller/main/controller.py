"""
Defines the main controller of the CLI
"""
# Libraries
import sys
import logging
import core.log

from .parser import create_parser, create_parser_options
from .constants import LOGS_LEVELS, LOGS, LOG_DEFAULT,\
                                    TASK_DEFAULT
from .. import text_counter


def controller():
    # Arguments
    parser = create_parser_options(create_parser())
    args = parser.parse_known_args()[0]

    # Init logging
    core.log.init()
    LOGGER = logging.getLogger(__name__)

    # Set task and log_level
    task = args.task
    controller = None
    log_level = args.log_level

    # No task specified
    if task is None:
        # Check if help is wanted
        if args.help:
            parser.print_help()
            sys.exit(0)
        # Task is default
        task = TASK_DEFAULT

    # Change log level
    root_logger = logging.getLogger()
    root_logger.setLevel(LOGS_LEVELS[LOGS.index(log_level)])
    if log_level != LOG_DEFAULT:
        LOGGER.info("Changed log level to %s", log_level)

    # Switch task and parse
    if task == "text-counter" or task == "text-counter-strict":
        if task == "text-counter":
            LOGGER.info("Text-Counter implementation selected")
        else:
            LOGGER.info("Text-Counter [STRICT] implementation selected")
        controller = text_counter.controller
        parser = text_counter.create_full_parser()
    else:
        LOGGER.error("No valid task has been selected, check usage")
        sys.exit(1)

    # Check for help
    if args.help:
        parser.print_help()
        sys.exit(0)

    # Welcome
    LOGGER.info("Welcome to map-reduce testing")

    # Let control to controller
    controller(args)

    # Exiting
    LOGGER.info("Good bye!")
