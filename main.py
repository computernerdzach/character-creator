# from textwrap import fill
from random import randint
# from character import Character
import character


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
    char_race = get_race()
    char_class = get_class()

    a_person = character.Character(name=name, race=char_race, char_class=char_class)
    print(f'Your size is {a_person.size}.')
    print(f'Your speed is {a_person.speed}.')
    print(f'Your hit-die is {a_person.hit_die}.')

    print('Your starting equipment is:')
    for i, item in enumerate(a_person.starting_equipment):
        print(f'    {i+1}: {item} x {a_person.starting_equipment[item]}')

    print('Your proficiencies are:')
    for i, proficiency in enumerate(a_person.tool_proficiencies):
        print(f'    {i + 1}: {proficiency}')


    # a_person.roll_ability_scores()
    # a_person.set_ability_scores()

    # if char_race == 'dragonborn':
    #     a_person = Dragonborn(name=name)
    #
    # if char_class == 'barbarian':
    #     a_barb = Barbarian(a_person)
    # print(a_person.name)
    # print(a_person.size)
    # print(a_person.speed)
    # print(a_person.STR)
    # ages = a_person.age_range
    # print(f"You can adventure between {ages[0]} and {ages[1]} years old.")
    # print("You have the following languages:")
    # for each in a_barb.languages:
    #     print(each)
    #
    # print("You have the following traits:")
    # for each in a_barb.traits:
    #     print(each.replace('-', ' '))
    #
    # print("You have selected the following proficiency bonuses:")
    # print(a_barb.proficiencies)


if __name__ == '__main__':
    main()
