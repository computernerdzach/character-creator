# TODO Add other races after HILL DWARF
races = {
    'Hill Dwarf': {
        'ability_increase': {
            'CON': 2, 'WIS': 1
        },
        'age_range': {
            'floor': 50, 'ceiling': 350
        },
        'alignment': '''Most dwarves are lawful, believing firmly in the benefits of a well-ordered
                        society. They tend toward good as well, with a strong sense of fair play and a
                        belief that everyone deserves to share in the benefits of a just order.
                     ''',
        'size': 'medium',
        'height': {
            'floor': 4, 'ceiling': 5
        },
        'weight': 150,
        'speed': 30,
        'proficiencies': {
            'weapon': ('battleaxe', 'handaxe', 'light hammer', 'warhammer'),
            'tool': ("smith's tools", "brewer's tools", "mason's tools"),
            'language': ('dwarven', 'common')
        },
        'resistances': {
            'saving throws': 'poison', 'damage': 'poison'
        },
        'other traits': {
            'stone cunning': '''Whenever you make an Intelligence (History) check related to
                                the origin of stonework, you are considered proficient in
                                the History skill and add double your proficiency bonus to
                                the check, instead of your normal proficiency bonus.
                             ''',
            'dark vision': '''You have superior vision in dark and dim conditions. You can
                              see in dim light within 60 feet of you as if it were bright
                              light, and in darkness as if it were dim light. You cannot
                              discern color in darkness, only shades of gray.
                           '''
        },
        'other_bonuses': {
            'hp': 1
        },
        'racial_spells': ()
    },
    'High Elf': 'XXXXXX'
}