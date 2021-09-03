import random
from argparse import ArgumentParser

from classes.Barbarian import Barbarian

from races.Dragonborn import Dragonborn
from races.Elf import Elf
from races.Halfling import Halfling
from races.Half_Orc import HalfOrc
from races.Dwarf import Dwarf
from races.Gnome import Gnome
from races.Half_Elf import HalfElf
from races.Human import Human
from races.Tiefling import Tiefling

RACE_MAPPING = {
    'dragonborn': Dragonborn,
    'elf': Elf,
    'halfling': Halfling,
    'half-orc': HalfOrc,
    'dwarf': Dwarf,
    'gnome': Gnome,
    'half-elf': HalfElf,
    'human': Human,
    'tiefling': Tiefling
}

CLASS_MAPPING = {
    'barbarian': Barbarian
}


class Character(object):
    # TODO add abstract methods

    def __init__(self, name, race, char_class):

        self.name = name
        self.race = RACE_MAPPING[race]()
        self.char_class = CLASS_MAPPING[char_class]()

        self.STR = 0
        self.DEX = 0
        self.INT = 0
        self.WIS = 0
        self.CHA = 0
        self.CON = 0

        self.languages = self.race.languages
        self.size = self.race.size
        self.speed = self.race.speed
        self.age_range = self.race.age_range
        self.traits = self.race.traits
        self.hit_die = self.char_class.hit_die
        self.tool_proficiencies = self.char_class.tool_proficiencies
        self.equipment = self.char_class.equipment
        self.proficiency_selections = self.char_class.proficiency_selections

    def set_ability_scores(self):
        self.__add_race_score_modifiers()

    def __add_race_score_modifiers(self):
        self.STR += self.race.score_modifiers['STR']
        self.DEX += self.race.score_modifiers['DEX']
        self.INT += self.race.score_modifiers['INT']
        self.WIS += self.race.score_modifiers['WIS']
        self.CHA += self.race.score_modifiers['CHA']
        self.CON += self.race.score_modifiers['CON']

    @staticmethod
    def __roll_ability_score():
        # Roll four 6-side die
        sample = random.sample(range(1, 6), 4)
        # Get the highest three rolls
        highest = sorted(sample)[-3:]
        # Record the total of the highest three
        return sum(highest)

    def roll_ability_scores(self):
        rolls = list()
        for x in range(6):
            rolls.append(self.__roll_ability_score())
        return rolls

    @property
    def ability_scores(self):
        return {
            'STR': self.STR,
            'DEX': self.DEX,
            'INT': self.INT,
            'WIS': self.WIS,
            'CHA': self.CHA,
            'CON': self.CON
        }

    @property
    def saving_throws(self) -> dict:
        vals = {'STR': 0,
                'DEX': 0,
                'INT': 0,
                'WIS': 0,
                'CON': 0,
                'CHA': 0}
        for key in self.char_class.saving_throws:
            vals[key] += self.char_class.proficiency_bonus + getattr(self, key)
        return vals


def create_character(name, race, char_class):
    char = Character(name, race, char_class)
    available_scores = char.roll_ability_scores()
    for ability_name in char.ability_scores.keys():
        success = False
        while not success:
            print(f'Set your {ability_name}...')
            print(f'Available scores: {available_scores}')
            choice = input()
            if not choice.isdigit():
                print('Selection must be an integer!')
                continue
            choice = int(choice)
            if choice not in available_scores:
                print('Invalid choice!')
            else:
                setattr(char, ability_name, choice)
                available_scores.remove(choice)
                success = True

    # TODO: User shouldn't need to call this; it should happen automatically.
    char.set_ability_scores()

    output = [f'{key}: {value}' for key, value in char.ability_scores.items()]
    print(', '.join(output))

    for attribute, value in char.__dict__.items():
        print(f'{attribute}: {value}')


if __name__ == '__main__':
    arg_parser = ArgumentParser('Create a character')
    arg_parser.add_argument('-n', '--name', required=True)
    arg_parser.add_argument('-r', '--race', required=True, choices=RACE_MAPPING.keys())
    arg_parser.add_argument('-c', '--char-class', required=True, choices=CLASS_MAPPING.keys())
    args = arg_parser.parse_args()
