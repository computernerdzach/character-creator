from textwrap import fill
from random import randint

# Dictionaries

# TODO Add other races after HILL DWARF
races = {'Hill Dwarf': {'ability_increase': {'CON': 2, 'WIS': 1}, 'age_range': {'floor': 50, 'ceiling': 350},
                        'alignment': "Most dwarves are lawful, believing firmly in the benefits of a well-ordered "
                                     "society. They tend toward good as well, with a strong sense of fair play and a "
                                     "belief that everyone deserves to share in the benefits of a just order.",
                        'size': 'medium', 'height': {'floor': 4, 'ceiling': 5}, 'weight': 150, 'speed': 30,
                        'proficiencies': {'weapon': ('battleaxe', 'handaxe', 'light hammer', 'warhammer'),
                                          'tool': ("smith's tools", "brewer's tools", "mason's tools"),
                                          'language': ('dwarven', 'common')},
                        'resistances': {'saving throws': 'poison', 'damage': 'poison'},
                        'other traits': {'stone cunning': "Whenever you make an Intelligence (History) check related to"
                                                          "the origin of stonework, you are considered proficient in "
                                                          "the History skill and add double your proficiency bonus to "
                                                          "the check, instead of your normal proficiency bonus."},
                        'other_bonuses': {'hp': 1}, 'racial_spells': ()},
         'High Elf': 'XXXXXX'}

# TODO Add other classes after BARBARIAN
classes = {'Barbarian': {'hit_die': 12, 'hp_base': 12,
                         'proficiencies': {'armor': ('light armor', 'medium armor', 'shields'), 'tool': 'none',
                                           'saving throws': ('STR', 'CON'),
                                           'skills': {'amount': 2, 'choices':
                                                      ('animal handling', 'athletics', 'intimidation', 'nature',
                                                       'perception', 'survival')}},
                         'equipment': {'a': ('greataxe', 'any martial melee weapon'),
                                       'b': ('two handaxes', 'any simple weapon'),
                                       'c': "explorer's pack and four javelins"}, 'features':
                         {'rage': "In battle, you fight with primal ferocity. On your turn, you can enter a rage as"
                                  " a bonus action. While raging, you gain the following benefits if you aren’t "
                                  "wearing heavy armor: • You have advantage on Strength checks and Strength saving"
                                  " throws. • When you make a melee weapon attack using Strength, you gain a bonus "
                                  "to the damage roll that increases as you gain levels as a barbarian, as shown in"
                                  " the Rage Damage column of the Barbarian table. • You have resistance to "
                                  "bludgeoning, piercing, and slashing damage. If you are able to cast spells, you "
                                  "can’t cast them or concentrate on them while raging. Your rage lasts for 1 "
                                  "minute. It ends early if you are knocked unconscious or if your turn ends and "
                                  "you haven’t attacked a hostile creature since your last turn or taken damage "
                                  "since then. You can also end your rage on your turn as a bonus action. Once you "
                                  "have raged the number of times shown for your barbarian level in the Rages "
                                  "column of the Barbarian table, you must finish a long rest before you can rage "
                                  "again.",
                          'unarmored defense': "While you are not wearing any armor, your Armor Class equals 10 + "
                                               "your Dexterity modifier + your Constitution modifier. You can use a"
                                               " shield and still gain this benefit."}},
           'Bard': 'XXXXXX'}

# TODO Add other backgrounds after ACOLYTE
backgrounds = {'Acolyte': {'proficiencies': ('insight', 'religion'), 'language': 2,
                           'equipment': ('a holy symbol', 'a prayer book or wheel', '5 sticks incense', 'vestments',
                                         'set of common clothes'), 'gold': 15,
                           'features': {'shelter of the faithful':
                                        "As an acolyte, you command the respect of those who share your faith, and you "
                                        "can perform the religious ceremonies of your deity. You and your adventuring "
                                        "companions can expect to receive free healing and care at a temple, shrine, or"
                                        " other established presence of your faith, though you must provide any "
                                        "material components needed for spells. Those who share your religion will "
                                        "support you (but only you) at a modest lifestyle. You might also have ties to "
                                        "a specific temple dedicated to your chosen deity or pantheon, and you have a "
                                        "residence there. This could be the temple where you used to serve, if you "
                                        "remain on good terms with it, or a temple where you have found a new home. "
                                        "While near your temple, you can call upon the priests for assistance, provided"
                                        " the assistance you ask for is not hazardous and you remain in goodstanding "
                                        "with your temple."}}}

features = {'grappler': "• You have advantage on attack rolls against a creature you are grappling. • You can use your "
                        "action to try to pin a creature grappled by you. To do so, make another grapple check. If you "
                        "succeed, you and the creature are both restrained until the grapple ends."}


# TODO Assign stat values, pick proficiencies, distribute equipment and gold
class Character(object):

    stats = {'STR': {'stat': 0, 'mod': 0, 'skills': {'athletics': 0}},
             'DEX': {'stat': 0, 'mod': 0, 'skills': {'acrobatics': 0, 'sleight of hand': 0, 'stealth': 0}},
             'INT': {'stat': 0, 'mod': 0, 'skills': {'arcana': 0, 'history': 0, 'investigation': 0, 'nature': 0,
                                                     'religion': 0}},
             'WIS': {'stat': 0, 'mod': 0, 'skills': {'animal handling': 0, 'insight': 0, 'medicine': 0, 'perception': 0,
                                                     'survival': 0}},
             'CHA': {'stat': 0, 'mod': 0, 'skills': {'deception': 0, 'intimidation': 0, 'performance': 0,
                                                     'persuasion': 0}},
             'CON': {'stat': 0, 'mod': 0}}

    proficiencies = {'armor': (), 'weapon': (), 'tool': (), 'language': (), 'skills': (), 'bonus': 2}
    extra_languages = 0
    resistances = {'saving throws': (), 'damage': ()}
    other_traits = {}
    equipment = ()
    currency = {'gold': 0, 'silver': 0, 'copper': 0}
    features = {}

    def __init__(self, race, char_class, background, name):
        self.race = race
        self.char_class = char_class
        self.background = background
        self.name = name


def read_out(text):
    print(fill(text, width=120))


def roll_stats():
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


def assign_stats(character):
    # Racial stat bonuses
    for each in races[character.race]['ability_increase']:
        each_value = races[character.race]['ability_increase'][each]
        for every in character.stats:
            if each == every:
                character.stats[every]['stat'] += each_value
    # Generate ability scores
    print('You have the following ability scores: ')
    stats = roll_stats()
    for each in character.stats:
        i = 0
        for every in stats:
            print(f'[{i}: {every}] ', end="")
            i += 1
        print('')
        assign = input(f"Which score would you like to assign to {each}? [Please use index]")
        character.stats[each]['stat'] = int(stats[int(assign)])
        character.stats[each]['mod'] = (character.stats[each]['stat'] - 10) // 2
        stats.remove(stats[int(assign)])


def main():
    # SELECT RACE
    print('Please select a race from the list below. [INTEGERS ONLY PLEASE]')
    for i, each in enumerate(races):
        print(f'{i}: {each}')
    the_race = int(input('Selection: '))
    the_race = list(races)[the_race]
    print(f'You selected {the_race}')

    # SELECT CLASS
    print('Please select a class from the list below. [INTEGERS ONLY PLEASE]')
    for i, each in enumerate(classes):
        print(f'{i}: {each}')
    the_class = int(input('Selection: '))
    the_class = list(classes)[the_class]
    print(f'You selected {the_class}')

    # SELECT BACKGROUND
    print('Please select a background from the list below. [INTEGERS ONLY PLEASE]')
    for i, each in enumerate(backgrounds):
        print(f'{i}: {each}')
    the_background = int(input('Selection: '))
    the_background = list(backgrounds)[the_background]
    print(f'You selected {the_background}')

    # NAME CHARACTER
    print('Please name your character.')
    the_name = input('Name: ')
    print(f'You are named {the_name}')

    # Instantiate character object with race, class, and background selections
    a_person = Character(race=the_race, char_class=the_class, background=the_background, name=the_name)
    assign_stats(a_person)

    # TEST CODE
    # print(a_person.stats['CON'])
    # print(a_person.stats['WIS'])
#
    # quote = f"Your {a_person.race.lower()} {a_person.char_class.lower()} named {a_person.name} was a " \
    #         f"{a_person.background.lower()} before they began adventuring.\n"
    # read_out(quote)
#
    # read_out(backgrounds[the_background]['features']['shelter of the faithful'])
    for each in a_person.stats:
        print(f"{each}: {a_person.stats[each]}")


if __name__ == '__main__':
    main()
