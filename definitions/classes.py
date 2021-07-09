# TODO Add other classes after BARBARIAN
classes = {
    'Barbarian': {
        'hit_die': 12,
        'hp_base': 12,
        'proficiencies': {
            'armor': ('light armor', 'medium armor', 'shields'),
            'tool': list(),
            'saving throws': ('STR', 'CON'),
            'add_skills': {
                'amount': 2,
                'choices': ('animal handling', 'athletics', 'intimidation', 'nature', 'perception', 'survival')
            }
        },
        'equipment': {
            'a': ('greataxe', 'any martial melee weapon'),
            'b': ('two handaxes', 'any simple weapon'),
            'c': "explorer's pack and four javelins"
        },
        'features': {
            'rage': '''In battle, you fight with primal ferocity. On your turn, you can enter a rage as
                       a bonus action. While raging, you gain the following benefits if you aren’t
                       wearing heavy armor: • You have advantage on Strength checks and Strength saving
                       throws. • When you make a melee weapon attack using Strength, you gain a bonus
                       to the damage roll that increases as you gain levels as a barbarian, as shown in
                       the Rage Damage column of the Barbarian table. • You have resistance to
                       bludgeoning, piercing, and slashing damage. If you are able to cast spells, you
                       can’t cast them or concentrate on them while raging. Your rage lasts for 1
                       minute. It ends early if you are knocked unconscious or if your turn ends and
                       you haven’t attacked a hostile creature since your last turn or taken damage
                       since then. You can also end your rage on your turn as a bonus action. Once you
                       have raged the number of times shown for your barbarian level in the Rages
                       column of the Barbarian table, you must finish a long rest before you can rage
                       again.
                    ''',
            'unarmored defense': '''While you are not wearing any armor, your Armor Class equals 10 +
                                    your Dexterity modifier + your Constitution modifier. You can use a
                                    shield and still gain this benefit.
                                 '''
        }
    },
    'Bard': 'XXXXXX'
}
