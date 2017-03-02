"""
A WordFileSplitter takes a text-file (encoded in UTF-8 if nothing specified)
and reads the file while generating word splits
"""
# Libraries
from .file import FileSplitter
from ..trigger.close import CloseTrigger


class WordFileSplitter(FileSplitter):
    """
    Reads text from a text-file (encoded in UTF-8 by default) using the file
    reader and generate letter splits

    If not enough letters are found, they're saved to be sent along with the
    next found letters in the next line until no more words are found

    Attributes:
        _filename (str): the file to be read and split into letters
    """

    def _generateSplit(self, data):
        """
        Given some piece of text in the data argument, returns a split
        containing the letters of the data as a list

        Args:
            data (str): piece of text

        Returns:
            list: list of strings (split)
        """
        return data.split()


if __name__ == "__main__":
    # Pool definition
    pool = type("TestPool", (CloseTrigger,), {
        "add": lambda self, x: print("Added item to pool", x),
        "close": lambda self: print("All data read")
    })
    # Default params
    print("Testing default params of WordFileSplitter")
    splitter = WordFileSplitter("README.md", pool())
    splitter.read()
    # Setting read size
    print("Testing read_size of WordFileSplitter")
    splitter = WordFileSplitter("README.md", pool())
    splitter.read_size = 20
    splitter.read()
    # Setting read size and split size
    print("Testing read_size and split_size of WordFileSplitter")
    splitter = WordFileSplitter("README.md", pool())
    splitter.read_size = 20
    splitter.split_size = 10
    splitter.read()
