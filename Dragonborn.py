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


class Dragonborn(Race):

    def __init__(self):
        super().__init__()
        self.score_modifiers['STR'] += 2
        self.score_modifiers['CHA'] += 1
        self.languages.append('draconic')

    def __str__(self):
        return 'Dragonborn'

    @property
    def size(self):
        return 'medium'

    @property
    def speed(self):
        return 30

    @property
    def age_range(self):
        return [15, 80]

    @property
    def traits(self):
        return ['draconic-ancestry', 'breath-weapon', 'damage-resistance']
