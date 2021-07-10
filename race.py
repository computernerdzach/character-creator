from abc import ABC, abstractmethod
from Dragonborn import Dragonborn


class Race(ABC):
    def __init__(self, name, a_race):
        self.name = name
        self.aRace = a_race
        self.race_choices = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'HalfElf', 'HalfOrc', 'Human', 'Tiefling']

    @abstractmethod
    def get_name(self):
        print('Please name your character.')
        the_name = input('Name: ')
        print(f'You are named {the_name}')
        return the_name

    @abstractmethod
    def pick_race(self):
        # available_races: ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'HalfElf', 'HalfOrc', 'Human', 'Tiefling']
        print('Please select your race. [INT only please]')
        for i, choice in enumerate(Race.race_choices):
            print(f"{i}:    {choice}")
        the_race = input('Race: ')
        print(f"You have selected {the_race}")
        return the_race

    size = 'medium'
    hpMod = 0
    maxAge = 0
    age = 0
    speed = 30
    abilityIncreases = list()
    resistances = list()
    immunities = list()
    senses = list()
    skillProficiencies = list()
    savingThrowProf = list()
    weaponProf = list()
    toolProf = list()
    armorProf = list()
    languages = list()
    addtlTraits = dict()


