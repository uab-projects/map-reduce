"""
Defines the controller to guide the software workflow when choosing the text
counter module
"""
# Libraries
import logging
import sys
import os
from ..main import parser as main_parser
from .parser import create_parser, create_parser_options
from core.implements.text_counter import create_pools
from core.splitter import WordFileSplitter, LetterFileSplitter

# Constants
LOGGER = None
"""
    logging.Logger: module logger
"""


def show_result(result, filename=None):
    """
    Given the result of the map-reduce task, prints it as the teacher of the
    subject desires

    Args:
        result (dict): dictionary containing last reduce result
        filename (str): the file the result is from. If none, no file is
        printed
    """
    # Print file
    if filename is not None:
        print("%s:" % (filename))
    # Print counts
    for key, value in sorted(result.items()):
        print("      %d %s" % (value, key))


def controller(args):
    """
    Executes the controller for the text counter
    """
    # Init logger
    LOGGER = logging.getLogger("text_counter")

    # Get arguments
    parser = create_parser()
    main_parser.create_parser_options(parser)
    create_parser_options(parser)
    args = parser.parse_args()

    # Get input files
    files = args.input_files

    if args.merge:
        # Create pools
        LOGGER.info("Creating map-reduce merged process pools")
        pool = create_pools(lambda result: show_result(result, filename))

    # Check if they exist
    for filename in files:
        # Check file
        if not os.path.isfile(filename):
            LOGGER.critical("File %s doesn't exist", filename)
            sys.exit(1)

        if not args.merge:
            # Create pools
            LOGGER.info("Creating map-reduce process pools")
            pool = create_pools(lambda result: show_result(result, filename))

        # Create splitter
        LOGGER.info("Creating splitter")
        splitter_cls = WordFileSplitter
        if args.letters:
            LOGGER.info("Chosen letter file splitter")
            splitter_cls = LetterFileSplitter
        splitter = splitter_cls(files[0], pool)

        # Read and execute
        LOGGER.info("Starting map-reduce tasks")
        splitter.read()

        if not args.merge:
            splitter.pool.close()
            # Wait until finish
            pool.join()
            LOGGER.info("Finished map-reduce tasks")

    if args.merge:
        # Wait until finish
        splitter.pool.close()
        pool.join()
        LOGGER.info("Finished map-reduce merged tasks")
