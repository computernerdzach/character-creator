# from textwrap import fill
from random import randint
# from character import Character
from Dragonborn import Dragonborn
from Barbarian import Barbarian


def roll_stats():
    i, j = 0, 0
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


def get_name():
    print('Please name your character.')
    the_name = input('Name: ')
    print(f'You are named {the_name}')
    return the_name


def get_race():
    races = ('dragonborn', 'dwarf', 'elf', 'gnome', 'half-elf',
             'half-orc', 'halfling', 'human', 'tiefling')
    print('Please select a race from the list below. [INTEGERS ONLY PLEASE]')
    for i, each in enumerate(races):
        print(f'{i}: {each}')
    the_race = int(input('Selection: '))
    the_race = list(races)[the_race]
    print(f'You selected {the_race}')
    return the_race


def get_class():
    classes = ('barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk',
               'paladin', 'ranger', 'rogue', 'sorcerer', 'warlock', 'wizard')
    print('Please select a class from the list below. [INTEGERS ONLY PLEASE]')
    for i, each in enumerate(classes):
        print(f'{i}: {each}')
    the_class = int(input('Selection: '))
    the_class = list(classes)[the_class]
    print(f'You selected {the_class}')
    return the_class


def main():
    name = get_name()
    # char_class = get_class()
    char_race = get_race()
    char_class = get_class()
    if char_race == 'dragonborn':
        a_person = Dragonborn(name=name)

    if char_class == 'barbarian':
        a_barb = Barbarian(a_person)
    print(a_person.name)
    print(a_person.size)
    print(a_person.speed)
    print(a_person.STR)
    ages = a_person.age_range
    print(f"You can adventure between {ages[0]} and {ages[1]} years old.")
    print("You have the following languages:")
    for each in a_barb.languages:
        print(each)

    print("You have the following traits:")
    for each in a_barb.traits:
        print(each.replace('-', ' '))

    print("You have selected the following proficiency bonuses:")
    print(a_barb.proficiencies)

    STR = a_barb.STR
    DEX = a_barb.DEX
    WIS = a_barb.WIS
    INT = a_barb.INT
    CHA = a_barb.CHA
    CON = a_barb.CON

    print(f"Strength: {STR}, Dexterity: {DEX}, Wisdom: {WIS}, Intelligence: {INT}, Charisma: {CHA}, Constitution: {CON}")

if __name__ == '__main__':
    main()
