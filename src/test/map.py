"""
Test for the map pool module.
"""

# Libraries
import logging
import random
import string
from ..core.pool.reduce import RedPool
from ..core.pool.map import MapPool
from ..core.implements.text_counter import map_task, reduce_task


# Constants
LOGGER = logging.getLogger(__name__)
"""
    logging.Logger: module logger
"""


# Methods
def simple_test():
    # Create the reduce pool
    LOGGER.info("Creating reduce pool")
    RP = RedPool(reduce_task)
    RP.on_done = lambda x: LOGGER.info("Test result: %s", str(x))
    LOGGER.info("Creating map pool")
    MP = MapPool(map_task, RP)

    # Add elements to the map pool
    LOGGER.info("Adding items")
    for i in range(100):
        MP.add([random.choice(string.ascii_lowercase) for _ in range(10)])
    # Close pool
    LOGGER.info("Closing pool")
    MP.close()
    # Wait
    MP.join()
    LOGGER.info("Test completed")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s][%(name)s][%(levelname)s] %(message)s"
    )
    simple_test()
