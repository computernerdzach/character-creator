from random import randint

from definitions.backgrounds import backgrounds
from definitions.classes import classes
from definitions.races import races


# TODO Assign stat values, distribute equipment and gold
class Character(object):

    CHOICE_MAPPINGS = {'races': races, 'classes': classes, 'backgrounds': backgrounds}

    stats = {'STR': {'stat': 0, 'mod': 0, 'skills': {'athletics': 0}},
             'DEX': {'stat': 0, 'mod': 0, 'skills': {'acrobatics': 0, 'sleight of hand': 0, 'stealth': 0}},
             'INT': {'stat': 0, 'mod': 0, 'skills': {'arcana': 0, 'history': 0, 'investigation': 0, 'nature': 0,
                                                     'religion': 0}},
             'WIS': {'stat': 0, 'mod': 0, 'skills': {'animal handling': 0, 'insight': 0, 'medicine': 0, 'perception': 0,
                                                     'survival': 0}},
             'CHA': {'stat': 0, 'mod': 0, 'skills': {'deception': 0, 'intimidation': 0, 'performance': 0,
                                                     'persuasion': 0}},
             'CON': {'stat': 0, 'mod': 0}}

    proficiencies = {'armor': list(), 'weapon': list(), 'tool': list(),'language': list(), 'skills': list(),
                     'choices': list(), 'add_skills': {'choices': list(), 'amount': 0}}

    proficiency_mod = 2
    extra_languages = 0
    resistances = {'saving throws': list(), 'damage': list()}
    other_traits = {}
    equipment = list()
    currency = {'gold': 0, 'silver': 0, 'copper': 0}
    features = {}

    def __init__(self, race, char_class, background, name):
        self.race = race
        self.char_class = char_class
        self.background = background
        self.name = name

    @staticmethod
    def __roll_stats():
        i = 0
        j = 0
        all_scores = list()
        while j < 6:
            scores = list()
            while i < 4:
                scores.append(randint(0, 6))
                i += 1
            scores.remove(min(scores))
            all_scores.append(sum(scores))
            j += 1
            i = 0
        return all_scores

    def assign_stats(self):
        # Racial stat bonuses
        for each in races[self.race]['ability_increase']:
            each_value = races[self.race]['ability_increase'][each]
            for every in self.stats:
                if each == every:
                    self.stats[every]['stat'] += each_value
        # Generate ability scores
        print('You have the following ability scores: ')
        stats = self.__roll_stats()
        for each in self.stats:
            assigned = False
            # List Comprehension; it's cool
            choices = [f'[{i}: {every}]' for i, every in enumerate(stats)]
            print(' '.join(choices))
            while not assigned:
                # This exception catch will inform the user of an invalid selection and repeatedly ask for the same thing until a valid choice is given
                assign = input(f"Which score would you like to assign to {each}? [Please use index]")
                try:
                    self.stats[each]['stat'] = int(stats[int(assign)])
                except (IndexError, ValueError) as e:
                    print(f'Invalid selection: "{assign}". {e}')
                    continue
                self.stats[each]['mod'] = (self.stats[each]['stat'] - 10) // 2
                stats.remove(stats[int(assign)])
                # This boolean will only flip to True once this While block fully succeeds, finally breaking the loop
                assigned = True

    def calc_stats(self):
        raise NotImplementedError('calc_stats not implemented yet')

    def assign_proficiencies(self):
        # Racial proficiencies
        for each in races[self.race]['proficiencies']:
            each_value = races[self.race]['proficiencies'][each]
            for every in self.proficiencies:
                if each == every:
                    self.proficiencies[every].append(each_value)

        # Class proficiencies
        for each in classes[self.char_class]['proficiencies']:
            each_value = classes[self.char_class]['proficiencies'][each]
            for every in self.proficiencies:
                if each == every and each != 'add_skills':
                    self.proficiencies[every].append(each_value)
                elif each == every and each == 'add_skills':
                    self.proficiencies['add_skills']['amount'] += \
                        classes[self.char_class]['proficiencies']['add_skills']['amount']
                    more_choices = classes[self.char_class]['proficiencies']['add_skills']['choices']
                    for butt in more_choices:
                        self.proficiencies['add_skills']['choices'].append(butt)

        # print(f"Add'l skills to choose: {character.proficiencies['add_skills']['amount']}")

        # Background proficiencies
        for each in backgrounds[self.background]['proficiencies']:
            each_value = backgrounds[self.background]['proficiencies'][each]
            for every in self.proficiencies:
                if each == every and each != 'add_skills':
                    self.proficiencies[every].append(each_value)
                elif each == every and each == 'add_skills':
                    self.proficiencies['add_skills']['amount'] += \
                        backgrounds[self.background]['proficiencies']['add_skills']['amount']

        # Additional skill proficiencies
        print(self.stats)
        amount = self.proficiencies['add_skills']['amount']
        i = 0
        while i < amount:
            left = amount - i
            print(f"You have {left} more proficiencies to select. Please choose one from below:")
            choices = list(self.proficiencies['add_skills']['choices'])
            has = self.proficiencies['skills']
            for each in choices:
                if each in has:
                    choices.remove(each)
            j = 0
            for each in choices:
                print(f"{j}: {each}")
                j += 1
            selection = int(input('Selection: '))
            self.proficiencies['skills'].append(choices[selection])
            selected = choices[selection]
            for nanny in choices:
                if nanny == selected:
                    choices.remove(nanny)
            for ability in self.stats:
                for skill in self.stats[ability]:
                    if skill == 'skills':
                        for tech in self.stats[ability][skill]:
                            if tech == selected:
                                self.stats[ability][skill][tech] += self.proficiency_mod
            i += 1
            for each in self.stats:
                for every in each:
                    if every == 'skills':
                        print(f"{self.stats[each][every]}")