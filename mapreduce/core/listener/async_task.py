"""
Defines listeners for an asynchronous task. With asynchronous tasks, we don't
know either when the task starts to be performed or when the task is completed,
with errors or succesfully.

This listeners allow to model what an asynchronous task can notify. Therefore
depending on the implementation we can modify its functionality.
"""
# Libraries
from abc import abstractmethod


class AsyncTask(object):
    """
    An asynchronous task is a task that is scheduled to run, without knowing
    when the task will start running or end running. Therefore the events
    defined here allow to model the events we can be notified with asynchronous
    tasks.
    """

    @abstractmethod
    def _on_task_start(self):
        """
        Listener that will be called when the task starts running
        """
        pass

    @abstractmethod
    def _on_task_fail(self):
        """
        Listener that will be called when the task has been executed some error
        or Exception was risen.

        By default, calls on_task_complete to be notified task has completed
        """
        self._on_task_complete()

    @abstractmethod
    def _on_task_success(self):
        """
        Listener that will be called when the task has been executed
        successfully without errors

        By default, calls on_task_complete to be notified task has completed
        """
        self._on_task_complete()

    @abstractmethod
    def _on_task_complete(self):
        """
        Listener that will be called when the task has been executed either
        successfully or not
        """
        pass
