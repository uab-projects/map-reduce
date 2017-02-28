"""
Defines a Pool used to apply map tasks in the map-reduce paradigm. So that
class is ready to do the proper task and transfer its result to the reduce
stage. This way, once the task to do is already completed the result will be
inmediately passed to the next Pool.
"""
from .basic import BasicPool
import logging


# Constants
LOGGER = logging.getLogger(__name__)
"""
    logging.Logger: module logger
"""


class MapPool(BasicPool):
    """
    Implements a pool ready to perform map kind tasks, meaning that will take
    only a piece of the big real work to process.

    Attributes:
        _nextStep (multiprocessing.Pool): next step in the workflow to transfer
        the data once the proper work is already done
    """
    __slots__ = ["_nextStep"]

    def __init__(self, task, nextStep):
        """
        Initializes the map pool
        """
        super().__init__(task)
        self._nextStep = nextStep

    def _on_task_success(self, result):
        """
        Sends the result, once processed successfully to the next stage of the
        main application to do the proper thing.
        """
        self._nextStep.add(result)
        super()._on_task_success(result)

    def _on_done(self):
        """
        Tells the next stage that will not be more entries.
        """
        self._nextStep.close()
        self._nextStep.join()
        LOGGER.info("Map stage completed")
