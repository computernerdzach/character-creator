from abc import ABC, abstractmethod


class Race(ABC):
    def __init__(self, name):
        self.name = name
        self.STR = 0
        self.DEX = 0
        self.INT = 0
        self.WIS = 0
        self.CHA = 0
        self.CON = 0
