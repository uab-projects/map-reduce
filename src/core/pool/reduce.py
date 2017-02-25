"""
Defines a Pool used to apply reduce tasks in the map-reduce paradigm. This way,
groups of items are stored until they can be reduced together and the process
is stoped when no more data is incoming and all reduce operations have finished

The reduce operation implies that the result of the task will be added again to
the pool to be reduced until no more items can be reduced. This means that is
a feedback pool.
"""
from .basic import BasicPool
import logging


# Constants
LOGGER = logging.getLogger(__name__)
"""
    logging.Logger: module logger
"""
DEFAULT_MIN_GROUP_SIZE = 2
"""
    int: minimum number of elements that have to be present to perform a
    reduce operation
"""


class RedPool(BasicPool):
    """
    Implements a pool that is prepared to perform reduce tasks, that mean that
    will take n items and return 1 as exchange that will have to be reduced
    further with other incoming items.

    When all items have been received and all items have been reduced, the
    _on_done event is triggered, passing the result to the on_done property

    Attributes:
        _ready (list): list of items waiting for be reduced
        _subpool (RedPool): next pool where reduces will go
        _group_size (int): number of items to group to apply a reduce task
        _user_on_done (function): method to call when the reduce operation
                                  has finished
                                  the result will be passed as argument
    """
    __slots__ = ["_ready", "_subpool", "_group_size", "_user_on_done", "_i"]

    def __init__(self, task, i=0):
        """
        Initializes the reduce pool with an empty list of pending items and
        noop for the _user_on_done function
        """
        super().__init__(task)
        self._ready = []
        self._subpool = None
        self._i = i
        self._group_size = DEFAULT_MIN_GROUP_SIZE
        self._user_on_done = lambda: None

    def add(self, item):
        """
        Checks if there are enough items to send them to perform the reduce
        task, and if not, sends the item to a buffer.

        When no more items are incoming, the minimum size for reduce operation
        is ignored.
        """
        LOGGER.debug("[P%02d] Adding new item to reduce: %s", self._i,
                     str(item))
        # Append to ready queue
        self._ready.append(item)

        # Check if enough items to reduce
        if len(self._ready) < self._group_size:
            LOGGER.debug("[P%02d] Queuing reduce pool item: %s", self._i,
                         str(item))
        else:
            LOGGER.debug("[P%02d] Sending %d items to reduce", self._i,
                         len(self._ready))
            # Copy arguments list
            item_list = tuple(self._ready)
            self._ready = []
            # Add to pool
            # Count scheduled task
            self._scheduled += 1
            # Launch task
            self._pool.apply_async(
                self._task,
                item_list,
                {},
                self._on_task_success, self._on_task_fail
            )

    def _on_done(self):
        """
        Calls the user-defined function with the result of the reduce
        """
        # Check if there's something remaining in the ready queue
        if len(self._ready) > 0:
            LOGGER.debug("[P%02d] Adding pending work to subpool", self._i)
            self._subpool.add(self._ready[0])
            self._ready = []
        # Wait for subpool to finish
        LOGGER.debug("[P%02d] Waiting for subpool %d to finish", self._i,
                     self._i+1)
        self._subpool.close()
        if self._subpool.scheduled > 0:
            self._subpool.join()
        self._user_on_done(self._ready)
        LOGGER.debug("[P%02d] Finished subpool %d", self._i, self._i+1)

    def _on_task_success(self, result):
        """
        Logs that a task has completed its execution and increments that
        counter. After that, calls to the _on_task_complete, the default
        behaviour

        Args:
            result (object): result returned by the task
        """
        # Create subpool to add work if don't exit
        if self._subpool is None:
            LOGGER.debug("[P%02d] Creating subpool %d for recursive reduces",
                         self._i, self._i+1)
            self._subpool = self.__class__(self._task, self._i+1)
            self._subpool.on_done = self._user_on_done
        # Add work to subpool
        self._subpool.add(result)
        super()._on_task_success(result)

    @property
    def on_done(self):
        """ Returns the _user_on_done attribute """
        return self._user_on_done

    @on_done.setter
    def on_done(self, on_done):
        """ Sets the _user_on_done attribute """
        self._user_on_done = on_done

    @property
    def group_size(self):
        """ Returns the _group_size attribute """
        return self._group_size

    @group_size.setter
    def group_size(self, group_size):
        """ Sets the _group_size attribute """
        self._group_size = group_size
