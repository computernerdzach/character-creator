from textwrap import fill
from random import randint
from race import Race
from Dragonborn import Dragonborn


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


def get_class():
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
    a_person = Dragonborn(name=name)
    # print(a_person.name)
    # print(a_person.size)
    # print(a_person.speed)
    # print(a_person.STR)
    # ages = a_person.age_range
    # print(f"You can adventure between {ages[0]} and {ages[1]} years old.")
    print("You have the following languages:")
    for each in a_person.languages:
        print(each)

    print("You have the following traits:")
    for each in a_person.traits:
        print(each.replace('-', ' '))


if __name__ == '__main__':
    main()


