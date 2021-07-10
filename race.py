from abc import ABC, abstractmethod


class Race(ABC):
    def __init__(self, name):
        self.name = name
        self.aRace = a_race
        self.race_choices = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'HalfElf', 'HalfOrc', 'Human', 'Tiefling']

    def pick_race(self):
        # available_races: ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'HalfElf', 'HalfOrc', 'Human', 'Tiefling']
        print('Please select your race. [INT only please]')
        for i, choice in enumerate(self.race_choices):
            print(f"{i}:    {choice}")
        the_race = int(input('Race: '))
        print(f"You have selected {self.race_choices[the_race]}")
        return self.race_choices[the_race]

    @property
    @abstractmethod
    def size(self):
        pass

    # size = 'medium'
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


