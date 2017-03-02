"""
Generic structure to use when defining a splitter in a map-reduce programming
paradigm
"""
from abc import abstractmethod
from ..listener.done import DoneListener

# Constants
SPLIT_SIZE_DEFAULT = 1
"""
    int: default split size, see AbstractSplitter for more
"""

class AbstractSplitter(DoneListener):
    """
    Interface for defining splitter classes

    Attributes:
        _pool (AbstractPool): the pool where to send the splitted pieces
        _split_size (int): minimum split size to send. until split is not the
        minimum size specified here, it will be buffered
    """
    __slots__ = ["_pool", "_split_size"]

    def __init__(self, pool):
        """
        Initializes the splitter with the pool where the splitted pieces read
        will be sent to be processed, commonly by a map procedure

        Args:
            pool (AbstractPool): pool where to send splits
        """
        self._pool = pool
        self._split_size = SPLIT_SIZE_DEFAULT

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
        pass

    @property
    def pool(self):
        """ Returns the pool where the splits are sent """
        return self._pool

    @property
    def split_size(self):
        """ Returns the split size """
        return self._split_size

    @split_size.setter
    def split_size(self, split_size):
        """ Sets the split size """
        self._split_size = split_size
