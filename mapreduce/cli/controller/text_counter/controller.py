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
from core.implements import text_counter, text_counter_strict
from core.splitter import WordFileSplitter, LetterFileSplitter


def show_result(result, no_out=False, filename=None):
    """
    Given the result of the map-reduce task, prints it as the teacher of the
    subject desires

    Args:
        result (dict): dictionary containing last reduce result
        no_out (bool): show just the amount
        filename (str): the file the result is from. If none, no file is
        printed
    """
    # Convert to dictionary
    if isinstance(result, list):
        result_dict = {}
        for map_tuple in result:
            key, val = map_tuple
            result_dict[key] = val
        result = result_dict
    if no_out:
        print("A total of %d items reduced", len(result.keys()))
    else:
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
    implement = text_counter if args.task == "text-counter" \
        else text_counter_strict
    LOGGER.info("Selected implementation is %s", implement.__name__)

    # Get input files
    files = args.input_files
    pools = []

    # Create unique pool for merged files option
    if args.merge:
        # Create pools
        LOGGER.info("Creating map-reduce merged process pools")
        pools.append(implement.create_pools(
            lambda r: show_result(r, args.no_out)))

    # Loop files
    for filename in files:
        # Check file
        if not os.path.isfile(filename):
            LOGGER.critical("File %s doesn't exist", filename)
            sys.exit(1)

        # Create pool per file if not merged
        if not args.merge:
            # No filename if just one specified
            filename_print = filename if len(files) > 1 else None
            # Create pools
            LOGGER.info("Creating map-reduce process pools")
            pools.append(implement.create_pools(
                lambda r: show_result(r, args.no_out, filename_print)))

        # Pick pool
        pool = pools[-1]

        # Create splitter
        LOGGER.info("Creating splitter")
        splitter_cls = WordFileSplitter
        if args.letters:
            LOGGER.info("Chosen letter file splitter")
            splitter_cls = LetterFileSplitter
        splitter = splitter_cls(filename, pool)

        # Customize splitter
        splitter.read_size = args.read_size
        splitter.split_size = args.split_size

        # Read and execute
        LOGGER.info("Starting map-reduce tasks")
        splitter.read()

        # Close data source for file if not merged
        if not args.merge:
            splitter.pool.close()

    # Close general pool if merged
    if args.merge:
        splitter.pool.close()

    # Join all pools
    for pool in pools:
        pool.join()

    # Finished
    LOGGER.info("Finished map-reduce tasks")
