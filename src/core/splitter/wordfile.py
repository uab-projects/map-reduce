"""
A WordFileSplitter takes a text-file (encoded in UTF-8 if nothing specified)
and reads the file by lines or until a limit is reached and sends a defined
group of words to the splitter
"""
# Libraries
from .file import FileSplitter
from ..trigger.close import CloseTrigger

# Constants
DEFAULT_ENCODING = "utf-8"
"""
    str: default encoding to use in the splitter if no encoding is specified
"""
DEFAULT_NWORDS = 1
"""
    int: default number of words to send per group
"""


class WordFileSplitter(FileSplitter):
    """
    Reads text from a text-file (encoded in UTF-8 by default) sequentially
    until a line ending character is found then with that piece of text, a
    split is tried to make using the words in the line

    If not enough words are found, they're saved to be sent along with the next
    found words in the next line until no more words are found

    Attributes:
        _filename (str): the file to be read and split into words
        _n_words (int): number of words per split to be sent to the pool if
        less than _n_words are found in the line or buffer. If is 0, group of
        words from the line is sent no matter how many words are there
        split is sent if has _n_words
    """
    __slots__ = ["_filename", "_n_words"]

    def __init__(self, filename, pool):
        """
        Inits a file splitter with the filename to read and the pool where to
        send the splits to

        Args:
            filename (str): the file to read and split
            pool (AbstractPool): the pool to use to send splits when reading
        """
        super().__init__(self, pool)
        self._filename = filename
        self._n_words = DEFAULT_NWORDS

    def _openFile(self):
        """
        Opens the file given the filename and returns a io.TextIOWrapper
        instance

        Raises:
            FileNotFoundError: if file is not found

        Returns:
            object: file-like object
        """
        return open(self._filename, "rt", encoding="UTF-8", errors="ignore")

    def _readFile(self, file_obj):
        """
        Reads the file-like object (subclass of class io.TextIOWrapper) and
        while reading, goes sending splits to the pool
        """
        # Read first line
        line = file_obj.readline()
        split = []
        file_ended = line == ""
        # Read next ones
        while not file_ended:
            # Get words from the line and append them to split
            split += line.split()
            # If split is big enough, send it
            if(len(split) > self._n_words):
                self._pool.add(split)
                split = []
            # Get next line
            line = file_obj.readline()
            file_ended = line == ""

        # Send last split
        if len(split):
            self._pool.add(split)

    @property
    def n_words(self):
        """ Returns the _n_words attribute """
        return self._n_words

    @n_words.setter
    def n_words(self, n_words):
        """ Sets the _n_words attribute """
        self._n_words = n_words


if __name__ == "__main__":
    pool = type("TestPool", (CloseTrigger,), {
        "add": lambda self, x: print("Added item to pool", x),
        "close": lambda self: print("All data read")
    })
    splitter = WordFileSplitter("README.md", pool())
    splitter.read()
