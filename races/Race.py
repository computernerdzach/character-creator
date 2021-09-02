from abc import ABC, abstractmethod


class Race(ABC):
    def __init__(self):
        self.score_modifiers = {
            'STR': 0,
            'DEX': 0,
            'INT': 0,
            'WIS': 0,
            'CHA': 0,
            'CON': 0
        }
        self.languages = ['common']

    @property
    @abstractmethod
    def size(self):
        pass

    @property
    @abstractmethod
    def speed(self):
        pass

    @property
    @abstractmethod
    def age_range(self):
        pass

    @property
    @abstractmethod
    def traits(self):
        pass
