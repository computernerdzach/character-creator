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


def char_sheet(player):
    print('-----     -----     -----')
    print(
        f'Name: {player.name}    |Race: {player.race}    |Class: {player.char_class}\n'
        f'Size: {player.size}    |Speed: {player.speed}    |Hitdie: {player.hit_die}\n')
    print('You have the following equipment:')
    for equipment in player.equipment:
        print(f'    {equipment}: x{player.equipment[equipment]}')
    print('')
    print('Your tool and skill proficiencies are:')
    print('  Tool -')
    for tool in player.tool_proficiencies:
        print(f'    {tool}')
    print('')
    print('  Skill -')
    for skill in player.proficiencies:
        print(f'    {skill}')


def main():
    name = get_name()
    char_race = get_race()
    char_class = get_class()

    a_person = character.Character(name=name, race=char_race, char_class=char_class)
    char_sheet(a_person)


if __name__ == '__main__':
    main()
