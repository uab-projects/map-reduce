"""
Test for the reduce module.
"""
# Libraries
from ..core.pool.reduce import RedPool
from ..core.listener.done import DoneListener
import multiprocessing


# Methods
def simple_test():
    # Creating the listener
    RP = None
    DL = type("FinishListener", (DoneListener, ), {
        "done": lambda self: print("test passed")
    })()

    # Creating the pool
    RP = RedPool(DL)

    # Adding elements to the pool
    aux = {"a": 3, "b": 2}
    RP.add(aux)

    aux = {"c": 3, "d": 7}
    RP.add(aux)

    # aux = {"a": 2, "d": 3}
    # RP.add(aux)
    RP.done()
    RP.wait()


if __name__ == "__main__":
    simple_test()
