from abc import ABC, abstractmethod


class CharClass(ABC):
    def __init__(self):
        self.proficiency_quantity = 0
        self.class_proficiencies = {
            'weapon': [],
            'armor': [],
            'language': [],
            'instrument': []
        }
        self.saving_throws = {
            'STR': 0,
            'DEX': 0,
            'INT': 0,
            'WIS': 0,
            'CHA': 0,
            'CON': 0
        }
        self.starting_equipment = {
            'pack': '',
            'weapons': [],
            'armor': [],
            'other': []
        }
        self.sub_classes = []
        self.spells_bool = True
