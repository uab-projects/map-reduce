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
def join_dicts(item1, item2):
    """
    Converges the keys for the two items received
    """
    dic = {}
    for k in (set(list(item1.keys())+list(item2.keys()))):
        dic[k] = item1.get(k, 0) + item2.get(k, 0)

    return dic


# Methods
def simple_test():
    # Creating the pool
    LOGGER.info("Creating reduce pool")
    reduce_pool = RedPool(join_dicts)
    reduce_pool.on_done = lambda x: LOGGER.info("Test result: %s", str(x))

    # Adding elements to the pool
    LOGGER.info("Adding items")
    for i in range(20):
        reduce_pool.add({"a": 1, "b": 1})

    # Close pool
    LOGGER.info("Closing pool")
    reduce_pool.close()

    # Wait to finish pool
    reduce_pool.join()
    LOGGER.info("Done testing")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)s][%(name)s][%(levelname)s] %(message)s"
    )
    simple_test()
