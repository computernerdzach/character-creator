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
    print('')
    print('--STATS--')
    for stat in player.stats:
        print(f'{stat}: {player.stats[stat]}')


def assign_stats(raw_stats, player):
    the_stats = raw_stats
    assigned_stats = {'STR': 0,
                      'DEX': 0,
                      'INT': 0,
                      'WIS': 0,
                      'CHA': 0,
                      'CON': 0}

    labels = list(assigned_stats.keys())
    unassigned = the_stats

    j = 0
    while j < len(assigned_stats):

        print(f'Here are your unassigned rolls:')
        for i, stat in enumerate(unassigned):
            print(f'    {i}: {stat}')

        print(f'Here are your unassigned stats:')
        for k, label in enumerate(labels):
            if player.stats[label] == 0:
                print(f'    {k}: {label}')

        user_number = int(input('Which roll would you like to use?\n-> '))
        user_stat = int(input('Which stat would you like to apply it to?\n-> '))

        key = labels[user_stat]
        value = unassigned[user_number]
        player.stats[key] = value

        labels.remove(key)
        unassigned.remove(value)

        j += 1
    # return assigned_stats
    # player_stats = player.stats
    # while len(assigned_stats) > 0:
    #     for picked_stat in assigned_stats:
    #         for character_stat in player_stats:
    #             if picked_stat == character_stat:
    #                 player.stats[character_stat] = assigned_stats[picked_stat]
    #                 assigned_stats.pop(picked_stat)
    #                 player_stats.pop(character_stat)




def main():
    name = get_name()
    char_race = get_race()
    char_class = get_class()

    a_person = character.Character(name=name, race=char_race, char_class=char_class)

    player_stats = roll_stats()
    assign_stats(player_stats, a_person)

    char_sheet(a_person)


if __name__ == '__main__':
    main()
