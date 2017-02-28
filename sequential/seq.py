"""
Sequential implementation of the same application, easier to do
"""


class Abstract(object):
    """
    Common methods and atrributes
    """
    __slots__ = ["_queue", "_next"]

    def __init__(self, next_step=None):
        self._queue = []
        self._next = next_step

    def add(self, item):
        self._queue.append(item)

    def senddata(self, data):
        self._next.add(data)


class Map(Abstract):
    """
    Map class
    """

    def execute(self):
        """
        som
        """
        while len(self._queue) != 0:
            item = self._queue.pop(0)
            self.senddata(self.count(item))

    def count(self, item):
        """
        Counts the elements from the item passed as a parameter and puts them
        into a dictionary
        """
        dic = {}
        for it in item:
            dic[it] = dic.get(it, 0) + 1

        return dic


class Reduce(Abstract):
    """
    Reduce class
    """
    def execute(self):
        while len(self._queue) >= 2:
            it1, it2 = self._queue[0], self._queue[1]
            result = self.join(it1, it2)
            self._queue.remove(it1)
            self._queue.remove(it2)
            self._queue.append(result)

        if len(self._queue) == 1:
            self.senddata(self._queue[0])
        else:
            print("ERROR")

    def join(self, item1, item2):
        dic = {}
        for k in (set(list(item1.keys())+list(item2.keys()))):
            dic[k] = item1.get(k, 0) + item2.get(k, 0)

        return dic


class Finish(Abstract):
    def show(self):
        print("--> Final result", self._queue)


def test():
    f = Finish()
    r = Reduce(f)
    m = Map(r)

    aux = ["a", "b", "c"]
    m.add(aux)

    aux = ["d", "f", "g"]
    m.add(aux)

    aux = ["d", "b", "g"]
    m.add(aux)
    m.execute()

    r.execute()

    f.show()


if __name__ == "__main__":
    test()
