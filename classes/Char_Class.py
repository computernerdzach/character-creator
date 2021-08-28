from abc import ABC, abstractmethod


class CharClass(ABC):
    def __init__(self):

        self.hit_die = 0
        self.saving_throws = {'STR': 0, 'DEX': 0, 'INT': 0, 'WIS': 0, 'CON': 0, 'CHA': 0}
        self.proficiency_bonus = 2


        # self.proficiency_quantity = 0
        # self.class_proficiencies = {
        #     'weapon': [],
        #     'armor': [],
        #     'language': [],
        #     'instrument': []
        # }
        # self.saving_throws = {
        #     'STR': 0,
        #     'DEX': 0,
        #     'INT': 0,
        #     'WIS': 0,
        #     'CHA': 0,
        #     'CON': 0
        # }
        # self.starting_equipment = {
        #     'pack': '',
        #     'weapons': [],
        #     'armor': [],
        #     'other': []
        # }
        # self.sub_classes = []

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
    def skill_proficiencies(self):
        pass

    @property
    @abstractmethod
    def saving_throw_assignment(self):
        pass

    @property
    @abstractmethod
    def starting_equipment_assignment(self):
        pass

    @property
    @abstractmethod
    def sub_classes(self):
        pass

