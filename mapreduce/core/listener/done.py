"""
The done listener is for classes that need to trigger a done event. The done
event means that all tasks were performed and is ready to continue.

This is useful in asynchronous environments, where we don't know when the jobs
will be ready so we must define callbacks. This callback would be triggered in
that case when all jobs had finished.
"""
# Libraries
from abc import abstractmethod, ABCMeta


class DoneListener(object):
    """
    Defines a class that is able to process a triggered done event, meaning
    that when the trigger is called, all pending tasks have been executed
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def _on_done(self):
        """
        The method that overrides this will know that all tasks have been
        executed (maybe with errors). This method has to be triggered manually
        when the condition of having all tasks done is achieved.
        """
        pass
