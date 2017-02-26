"""
A FileSplitter defines the basic structure of a splitter that reads pieces from
a file and sends them to a map pool
"""
# Libraries
from abc import abstractmethod
from .abstract import AbstractSplitter


class FileSplitter(AbstractSplitter):
    """
    A concrete file splitter that reads data and splits it from a file source

    Attributes:
        _filename (str): the file to be read and split
    """
    __slots__ = ["_filename"]

    def __init__(self, filename, pool):
        """
        Inits a file splitter with the filename to read and the pool where to
        send the splits to

        Args:
            filename (str): the file to read and split
            pool (AbstractPool): the pool to use to send splits when reading
        """
        super().__init__(pool)
        self._filename = filename

    def read(self):
        """
        Opens the file, handles the control with the file-like object to the
        reader that will read it and split it

        Raises:
            FileNotFoundError: if no file is found
        """
        super().read()
        file_obj = self._openFile()
        self._readFile(file_obj)
        file_obj.close()
        self._on_done()

    @abstractmethod
    def _openFile(self):
        """
        Opens the file given the filename and returns a file-like object

        Returns:
            object: file-like object
        """
        pass

    @abstractmethod
    def _readFile(self, file_obj):
        """
        Reads the file-like object (subclass of class io.TextIOWrapper) and
        while reading, goes sending splits to the pool
        """
        pass
