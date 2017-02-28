"""
Generic structure to use when defining a splitter in a map-reduce programming
paradigm
"""
from abc import abstractmethod
from ..listener.done import DoneListener


class AbstractSplitter(DoneListener):
    """
    Interface for defining splitter classes

    Attributes:
        _pool (AbstractPool): the pool where to send the splitted pieces
    """
    __slots__ = ["_pool"]

    def __init__(self, pool):
        """
        Initializes the splitter with the pool where the splitted pieces read
        will be sent to be processed, commonly by a map procedure

        Args:
            pool (AbstractPool): pool where to send splits
        """
        self._pool = pool

    @abstractmethod
    def read(self):
        """
        Reads by splits from source and goes sending splits to the pool,
        checking first that the pool exists

        Raises:
            AssertException: if pool is None when reading
        """
        assert self._pool is not None, "A pool must be defined before reading"

    def _on_done(self):
        """
        Triggered when all data has been read and splits have been sent, tells
        the pool that no more that is incoming
        """
        self._pool.close()

    @property
    def pool(self):
        """ Returns the pool where the splits are sent """
        return self._pool
