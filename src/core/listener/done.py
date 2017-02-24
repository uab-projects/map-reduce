"""
Defines a class that listens for a done event. The done event means, when
triggered, that a class that dynamically accepts data will receive no more
data after the event has been triggered manually.
"""
# Libraries
from abc import abstractmethod


class DoneListener(object):
    """
    Defines a class that is able to process a triggered done event, meaning
    that after the trigger no more data will be accepted

    Attributes:
        _done (bool): true if the done event has been triggered
    """
    __slots__ = ["_done"]

    def __init__(self):
        """
        Initializes the class with the done value set to false
        """
        self._done = False

    @abstractmethod
    def done(self):
        """
        When executed, we're telling the class that there will be no more
        incoming data. Here, default behaviour is set, that has to be done
        always and is to set the _done status to True as the event has been
        triggered (you can alter this if you want)
        """
        self._done = True

    def isDone(self):
        """
        Returns the status of the done event
        """
        return self._done
