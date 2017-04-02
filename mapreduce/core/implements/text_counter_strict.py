"""
Defines all the tasks to perform for a text_counter map reduce implementation
that accomplishes the text counting task in a strict map-reduce implementation
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
    Maps the list retrieved of the splitter that is supposed to be a list of
    words or letters into a key, value tuple list with the word or letter as
    key and the value 1 to follow a strict implementation of Map-Reduce

    Args:
        items (list): list of words or letters to pass into a map operation

    Returns:
        list: list of tuples where each tuple contains a key/value pair and
        each pair key is a word or letter and value is 1
    """
    res = []
    for item in items:
        res.append((item.lower(), 1))
    return res


def reduce_task(*items):
    """
    Reduces a number of map results items into a single list that sums all the
    tuples with the same key, summing their values

    items = [map_item_1, map_item_2, ...]
        where map_item_i =  [("hello", 1),("world", 1)...]

    Args:
        *items (list of lists): see previous itesm definition

    Returns:
        list: a map operation result list combining all the input lists and
        performing the sum operation on them to match equal keys and sum their
        values
    """
    merged = {}
    result = []
    # joined_list = reduce(lambda x, y: x.extend(y), items)
    for item in items:
        for map_tuple in item:
            word, count = map_tuple
            merged[word] = merged.get(word, 0) + count

    for key, val in merged.items():
        result.append((key, val))

    return result


def create_pools(finalize, reduce_size=-1):
    """
    Creates and concatenates the map and reduce pools,

    Args:
        finalize (function): last function called when reduce stage is
        completed
        reduce_size (int): reduce size to pass to reduce pools. if not
        specified, default is used

    Returns:
        multiprocessing.Pool: map stage pool with the link between reduce pool
        created
    """
    # Create the reduce pool
    LOGGER.debug("Creating reduce pool")
    reduce_pool = RedPool(reduce_task)

    # Set attributes
    reduce_pool.on_done = finalize
    if reduce_size > 1:
        reduce_pool.group_size = reduce_size

    # Create the map pool
    LOGGER.debug("Creating map pool")
    map_pool = MapPool(map_task, reduce_pool)

    return map_pool
