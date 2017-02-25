"""
Something
"""
from .abstract import AbstractPool

def do(a,b):
    print("doing",a,b)

def on_task_finish(result):
    f = open("test.txt","w")
    f.write("i'm done")
    f.close()
def on_task_error(result):
    f = open("test.txt","w")
    f.write(str(result))
    f.close()

class RedPool(AbstractPool):
    """
    Something
    """
    __slots__ = ["_ready"]

    def __init__(self, next_step):
        super().__init__()
        self._ready = None

    def __call__(self, item1, item2):
        """
        Converges the keys for the two items received
        """
        dic = {}
        for k in (set(list(item1.keys())+list(item2.keys()))):
            dic[k] = item1.get(k, 0) + item2.get(k, 0)

        return dic

    def on_task_finish(self, result):
        print("task done")
        #self._pending.remove(result)
        #self._check_stop()

    def add(self, item):
        """
        Something
        """
        print("Adding item")
        if self._ready is None:
            print("No ready item")
            self._ready = item
        else:
            print("Calling pool")
            aux = self._ready
            self._ready = None
            self._pending.append(self._pool.apply_async(
            self.execute,
            (item,aux),
            {},
            self.on_task_finish, on_task_error))

    def execute(self, item1, item2):
        """
        Something.
        """
        f = open("executing.txt","w")
        f.write("i'm done")
        f.close()
        #self.add(self(item1, item2))

    def do(self):
        f = open("putamadre.txt","w")
        f.write("i'm done")
        f.close()

    def _check_stop(self):
        """
        Something
        """
        print("Checking stop")
        if self._done and len(self._pending) == 0:
            print("Stop broh")
            self._next.done()

    def done(self):
        self._pool.close()

    def wait(self):
        """
        """
        self._pool.join()

    def getResult(self):
        """
        Returns the last result, should be called once the done is triggered
        """
        return self._ready
