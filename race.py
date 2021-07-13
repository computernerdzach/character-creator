from abc import ABC, abstractmethod
from random import randint


class Race(ABC):
    def __init__(self, name):
        self.name = name
        self.STR = 0
        self.DEX = 0
        self.INT = 0
        self.WIS = 0
        self.CHA = 0
        self.CON = 0

        self.roll_stats()

    # @property
    def roll_stats(self):
        i, j = 0, 0
        the_stats = list()
        while i < 6:
            each_stat = list()
            while j < 4:
                each_stat.append(randint(0, 6))
                j += 1
            each_stat.remove(each_stat(min))
            a_stat = sum(each_stat)
            i += 1
        print(the_stats)
