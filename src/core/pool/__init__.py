"""
This module defines the Pool model. We take the Pool meaning from the Python
multiprocessing library. A pool will be a class that accepts customized tasks
to be executed and executes them in parallel.

This pools are automated in a way that when the pool is defined, a task to
perform is defined, so to execute new tasks in parallel, just new data has to
be added to the pool and it will know what to perform, allowing dynamic data
entry with parallel multiprocessing.

Therefore the Pool is event oriented and will take help from listeners module
to know what kind of events the pool listens to.
"""
