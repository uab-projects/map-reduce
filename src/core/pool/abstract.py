"""
Something.
"""
from abc import ABCMeta, abstractmethod
from multiprocessing import Pool
from ..listener.done import DoneListener


class AbstractPool(DoneListener):
    """
    Something.
    """
    __slots__ = ["_next", "_pool", "_pending"]
    __metaclass__ = ABCMeta

    def __init__(self, next_step=None):
        """
        Something.
        """
        self._pool = Pool()
        self._pending = []
        self._next = next_step

    def add(self, item):
        """
        Adds a new element into the pool's queue.
        """
        self._pending.append(self._pool.apply_async(self.execute, item, {},
                             lambda result: self._pending.remove(result)))

    @abstractmethod
    def _check_stop(self):
        """
        Checks for stopping condition and tells the next one that will not
        receive more items, to be implemented.
        """

    def execute(self, item):
        """
        Something.
        """
        self._next.add(self(item))
        self._check_stop()

    @abstractmethod
    def __call__(self, item):
        """
        Task to by applied to the item, needed to be implemented.
        """
