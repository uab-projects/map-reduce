"""
Defines the controller to guide the software workflow when choosing the text
counter module
"""
# Libraries
import logging
import sys
import os
from .parser import PARSER
from core.implements.text_counter import create_pools
from core.splitter.wordfile import WordFileSplitter

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
    args = PARSER.parse_args()

    # Get input files
    files = args.input_files

    # Check if they exist
    for filename in files:
        # Check file
        if not os.path.isfile(filename):
            LOGGER.critical("File %s doesn't exist", filename)
            sys.exit(1)

        # Create pools
        LOGGER.info("Creating map-reduce process pools")
        pool = create_pools(lambda result: show_result(result, filename))

        # Create splitter
        LOGGER.info("Creating splitter")
        splitter = WordFileSplitter(files[0], pool)

        # Read and execute
        LOGGER.info("Starting map-reduce tasks")
        splitter.read()

        # Wait until finish
        pool.join()
        LOGGER.info("Finished map-reduce tasks")
