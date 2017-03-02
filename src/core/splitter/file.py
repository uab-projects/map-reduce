"""
A FileSplitter defines the basic structure of a splitter that reads pieces from
a file and sends them to a map pool
"""
# Libraries
from abc import abstractmethod
from .abstract import AbstractSplitter

# Constants
DEFAULT_ENCODING = "utf-8"
"""
    str: default encoding to use in the splitter if no encoding is specified
"""
DEFAULT_READ_SIZE = 0
"""
    int: number of characters to read from the file each time by default
"""


class FileSplitter(AbstractSplitter):
    """
    A concrete file splitter that reads data and splits it from a file source

    Attributes:
        _filename (str): the file to be read and split
        _read_size (int): number of characters to read from the file each
        time to create a buffer. If 0 is specified, a whole line is read
    """
    __slots__ = ["_filename", "_read_size"]

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
        self._read_size = DEFAULT_READ_SIZE

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
        Opens the file given the filename and returns a io.TextIOWrapper
        instance

        Raises:
            FileNotFoundError: if file is not found

        Returns:
            object: file-like object
        """
        return open(self._filename, "rt", encoding=DEFAULT_ENCODING,
                    errors="ignore")

    def _readData(self, file_obj):
        """
        Reads data from the file, as specified by property _read_size or a
        whole line is _read_size is 0

        If the end is a character, reads until a non-character is found

        Args:
            file_obj (object): file object to read

        Returns:
            str: read data
        """
        if self._read_size == 0:
            # Read by lines
            return file_obj.readline()
        else:
            # Read size
            data = file_obj.read(self._read_size)
            if data != "":
                last_char = data[-1]
                while last_char.isalpha():
                    data += file_obj.read(1)
                    last_char = data[-1]
            return data

    @abstractmethod
    def _generateSplit(self, data):
        """
        Given some piece of text in the data argument, the method must return
        a split generated with the data passed

        Args:
            data (str): piece of text

        Returns:
            list: list of strings (split)
        """
        pass

    def _readFile(self, file_obj):
        """
        Reads the file-like object (subclass of class io.TextIOWrapper) and
        while reading, goes sending splits to the pool
        """
        # Read first line
        data = self._readData(file_obj)
        split = []
        file_ended = data == ""
        # Read next ones
        while not file_ended:
            # Get words from the line and append them to split
            split += self._generateSplit(data)
            # If split is big enough, send it
            if(len(split) > self._split_size):
                self._pool.add(split)
                split = []
            # Get next line
            data = self._readData(file_obj)
            file_ended = data == ""

        # Send last split
        if len(split):
            self._pool.add(split)

    @property
    def read_size(self):
        """ Returns the read size """
        return self._read_size

    @read_size.setter
    def read_size(self, read_size):
        """ Sets the read size """
        if read_size >= 0:
            self._read_size = read_size
        else:
            raise ValueError("read_size must be positive or 0")
