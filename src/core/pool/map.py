"""
Something
"""
from .abstract import AbstractPool


class MapPool(AbstractPool):
    """
    Something
    """

    def __call__(self, items):
        """
        Something
        """
        dic = {}
        for item in items:
            dic[item] = dic.get(item, 0) + 1

        return dic

    def _check_stop(self):
        """
        Something
        """
        if self._done and not self._pending:
            self._next.done()
