from random import randint
from typing import Any


class CustomList(list):
    def random_pop(self) -> Any:
        if self.__len__() > 0:
            return self.pop(randint(0, self.__len__() - 1))
        return None
