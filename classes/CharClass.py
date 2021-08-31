from abc import ABC, abstractmethod


class CharClass(ABC):
    def __init__(self):

        self.proficiency_bonus = 2

    @property
    @abstractmethod
    def hit_die(self):
        pass

    @property
    @abstractmethod
    def tool_proficiencies(self):
        pass

    @property
    @abstractmethod
    def starting_equipment(self):
        pass

    @property
    @abstractmethod
    def sub_classes(self):
        pass

    @property
    @abstractmethod
    def saving_throws(self) -> list:
        pass
