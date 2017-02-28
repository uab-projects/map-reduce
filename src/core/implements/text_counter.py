"""
Defines all the tasks to perform for a text_counter map reduce implementation
"""
# Libraries
import logging
from ..pool.map import MapPool
from ..pool.reduce import RedPool

# Constants
LOGGER = logging.getLogger(__name__)
"""
    logging.Logger: module logger
"""


def map_task(items):
    """
    Creates a built-in python diccionary with the items received as a parameter
    as a key and counting the occurrences of the items as a value

    Args:
        items (list): items to work with, creating a key:value map with item
        and its occurrences
    """
    dic = {}
    for item in items:
        dic[item] = dic.get(item, 0) + 1

    return dic


def reduce_task(*items):
    """
    Converges the keys for the n items received, performing the sum operation
    with all the values of the same key and returning a joined dictionary

    Args:
        *args (dict): dictionaries to join summing their values with equal keys

    Returns:
        dict: merged dictionary
    """
    merged = dict()
    keys = set().union(*items)
    for key in keys:
        merged[key] = sum([x.get(key, 0) for x in items])
    return merged


def create_pools(finalize):
    """
    Creates and concatenates the map and reduce pools,

    Args:
        show_result (function): last function called when reduce stage is
        completed

    Returns:
        multiprocessing.Pool: map stage pool with the link between reduce pool
        created
    """
    # Create the reduce pool
    LOGGER.debug("Creating reduce pool")
    RP = RedPool(reduce_task)
    # Assign last task
    RP.on_done = finalize
    # Create the map pool
    LOGGER.debug("Creating map pool")
    MP = MapPool(map_task, RP)

    return MP
