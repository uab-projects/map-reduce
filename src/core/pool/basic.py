"""
Defines an abstract pool, this means, a generic pool that will start executing
the defined task when new data-items arrive, so will apply those data-items
to the task function.

Those tasks will be executed in parallel, with as much threads as the CPU is
able to handle. Therefore, the need for events of the Pool is obvious to know
when no more tasks will come and when all tasks have been completed.

Eventually, when the pool receives the close trigger, telling that no more data
will be incoming, the pool is closed and then the done method will be called

This is the most basic pool implementation that makes creating parallel tasks
easy
"""
from multiprocessing import Pool
import logging
from ..trigger.close import CloseTrigger
from ..listener.done import DoneListener
from ..listener.async_task import AsyncTask


# Constants
LOGGER = logging.getLogger(__name__)
"""
    logging.Logger: module logger
"""


class BasicPool(CloseTrigger, DoneListener, AsyncTask):
    """
    The basic pools is a pool that can accept tasks to perform, defined in the
    _task attribute and run them when new data-items arrive through the add
    method.

    Once no more data to be run is coming, the close method has to be manually
    triggered. Finally, the done event will be triggered when all tasks have
    been completed.

    Attributes:
        _pool (multiprocessing.Pool): pool of tasks to use
        _task (function): function to execute when adding new items to process
        _scheduled (int): number of tasks that have been scheduled, including
        the ones that have already been completed
        _succeeded (int): number of tasks that have completed successfully
        _failed (int): number of tasks that have completed but failed
    """
    __slots__ = ["_pool", "_task", "_scheduled", "_succeeded", "_failed"]

    def __init__(self, task):
        """
        Initializes the pool and the actual task pool with the task that the
        pool will have to perform when new items come

        Args:
            task (function): task the pool must perform in parallel
        """
        super().__init__()
        self._pool = Pool()
        self._task = task
        self._scheduled = 0
        self._succeeded = 0
        self._failed = 0

    def add(self, *args, **kwargs):
        """
        Adds a new item to be processed by the pool

        Args:
            *args: arguments to pass to the task to be executed
        """
        # Count scheduled task
        self._scheduled += 1
        # Launch task
        self._pool.apply_async(
            self._task,
            args,
            kwargs,
            self._on_task_success, self._on_task_fail
        )

    def close(self):
        """
        Closes the pool so no more external inputs will be able to be sent
        """
        super().close()
        self._pool.close()

    def join(self):
        """
        This is one of the most important functions with the pool. This has to
        be called to prevent execution finishes before all tasks are executed.

        Call to the method so the execution will be stopped until all tasks
        are executed (and therefore _on_done event is triggered)
        """
        self._pool.join()

    def _check_stop(self):
        """
        Checks if all tasks scheduled have been completed and no more data is
        going to arrive, so the done event can be triggered.
        """
        if self._closed and self._scheduled == self.completed:
            self._on_done()

    def _on_task_start(self):
        """
        Method to be executed when an asynchrounous task is starting to run.
        As there's no possible way for this to happen due to library
        limitations, this can't be implemented
        """
        raise NotImplementedError("""Method not implemented due to library
        limitations""")

    def _on_task_fail(self, exception):
        """
        Logs that a task has failed and increments that counter. After that,
        calls to the _on_task_complete, the default behaviour

        Args:
            exception (Exception): exception that caused the task to fail
        """
        self._failed += 1
        LOGGER.error("Task failed to execute: %s", str(exception))
        super()._on_task_fail()

    def _on_task_success(self, result):
        """
        Logs that a task has completed its execution and increments that
        counter. After that, calls to the _on_task_complete, the default
        behaviour

        Args:
            result (object): result returned by the task
        """
        self._succeeded += 1
        LOGGER.debug("Task done with result: %s", str(result))
        super()._on_task_success()

    def _on_task_complete(self):
        """
        After a task has completed, either with success or not, we have to
        detect if we have finished all tasks to trigger the done event
        """
        LOGGER.debug("Task completed")
        self._check_stop()

    @property
    def task(self):
        """ Returns the task set to perform """
        return self._task

    @property
    def scheduled(self):
        """ Returns the total tasks scheduled (completed tasks too) """
        return self._scheduled

    @property
    def succeeded(self):
        """ Returns the total tasks executed successfully """
        return self._succeeded

    @property
    def failed(self):
        """ Returns the total tasks executed that have failed """
        return self._failed

    @property
    def completed(self):
        """
        Returns the total tasks executed successfully or not, performing the
        sum of self._succeeded + self._failed
        """
        return self._succeeded + self._failed
