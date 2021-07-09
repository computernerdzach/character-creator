from textwrap import fill

from Character import Character


def read_out(text):
    print(fill(text, width=120))


def select_choices(key):
    mapping = Character.CHOICE_MAPPINGS[key]
    print(f'Please select a {key} from the list below. [INTEGERS ONLY PLEASE]')
    for i, each in enumerate(mapping):
        print(f'{i}: {each}')
    index = int(input('Selection: '))
    try:
        selection = list(mapping)[index]
        print(f'You selected {selection}')
    except IndexError as e:
        print(f'Invalid selection. {e}')
        # This exception catch uses "recursion" to call the function within itself every time this error is caught
        selection = select_choices(key)
    return selection


def name_character():
    # NAME CHARACTER
    print('Please name your character.')
    the_name = input('Name: ')
    print(f'You are named {the_name}')
    return the_name


def main():
    the_race = select_choices('races')
    the_class = select_choices('classes')
    the_background = select_choices('backgrounds')
    the_name = name_character()

    # Instantiate character object with race, class, and background selections
    a_person = Character(race=the_race, char_class=the_class, background=the_background, name=the_name)
    # a_person = Character(race='Hill Dwarf', char_class='Barbarian', background='Acolyte', name='Ben')

    try:
        a_person.assign_stats()
        a_person.assign_proficiencies()
        a_person.calc_stats()
    except NotImplementedError as error:
        print(f'{error}')

    # TEST CODE
    for each in a_person.stats:
        print(f"{each}: {a_person.stats[each]}")
    for each in a_person.proficiencies:
        print(f"{each}: {a_person.proficiencies[each]}")

    quote = f"Your {a_person.race.lower()} {a_person.char_class.lower()} named {a_person.name} was a " \
            f"{a_person.background.lower()} before they began adventuring.\n"
    read_out(quote)

    # print(a_person.stats['CON'])
    # print(a_person.stats['WIS'])


if __name__ == '__main__':
    main()
