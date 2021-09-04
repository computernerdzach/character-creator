from random import randint
import character


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
    print('')
    print('--STATS--')
    for stat in player.stats.keys:
        print(f'{stat}: {getattr(player.stats, stat)}')


def main():
    name = get_name()
    char_race = get_race()
    char_class = get_class()
    a_person = character.Character(name=name, race=char_race, char_class=char_class)
    char_sheet(a_person)


if __name__ == '__main__':
    main()
