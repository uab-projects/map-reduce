"""
Test for the reduce pool module.
"""
# Libraries
import logging
from ..core.pool.reduce import RedPool

# Constants
LOGGER = logging.getLogger(__name__)
"""
    logging.Logger: module logger
"""


# Reduce methods
def join_dicts(*items):
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


# Methods
def simple_test():
    # Creating the pool
    LOGGER.info("Creating reduce pool")
    reduce_pool = RedPool(join_dicts)
    reduce_pool.on_done = lambda x: LOGGER.info("Test result: %s", str(x))
    reduce_pool.group_size = 1000
    # Adding elements to the pool
    LOGGER.info("Adding items")
    for i in range(1000000):
        reduce_pool.add({"a": 1, "b": 1})

    # Close pool
    LOGGER.info("Closing pool")
    reduce_pool.close()

    # Wait to finish pool
    reduce_pool.join()
    LOGGER.info("Done testing")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s][%(name)s][%(levelname)s] %(message)s"
    )
    simple_test()
