"""
Defines a class that can be triggered a close event. The close event means,
when triggered, that a class that dynamically accepts data will receive no more
data after the event has been triggered manually.

It's name and meaning comes from the multiprocessing library, concretely from
the close method of the Pool class.
"""
# Libraries
from abc import abstractmethod, ABCMeta


class CloseTrigger(object):
    """
    Defines a class that is able to process a triggered close event, meaning
    that after the trigger no more data will be accepted.

    Also contains a boolean attribute to know if the trigger has been triggered

    Attributes:
        _closed (bool): true if the close event has been triggered
    """
    __slots__ = ["_closed"]
    __metaclass__ = ABCMeta

    def __init__(self):
        """
        Initializes the class with the close value set to false
        """
        self._closed = False

    @abstractmethod
    def close(self):
        """
        When executed, we're telling the class that there will be no more
        incoming data. Here, default behaviour is set, that has to be done
        always and is to set the _closed status to True as the event has been
        triggered (you can alter this if you want)
        """
        self._closed = True

    @property
    def closed(self):
        """ Returns the status of the close event """
        return self._closed
