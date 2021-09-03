from classes.CharClass import CharClass


class Barbarian(CharClass):
    # TODO: This should inherit from a parent class
    def __init__(self):

        super().__init__()

        self.equipment = self.pick_equipment(self.equipment_selections, self.starting_equipment)

    def __str__(self):
        return 'Barbarian'

    @property
    def hit_die(self):
        return 12

    @property
    def tool_proficiencies(self):
        return 'light-armor', 'medium-armor', 'shields', 'simple-weapons', 'martial-weapons'

    @property
    def proficiencies(self):
        choice = self.pick_proficiencies(self.proficiency_selections)
        return choice

    @property
    def saving_throws(self):
        return 'STR', 'CON'

    @property
    def proficiency_selections(self):
        return {2: ['animal-handling', 'athletics', 'intimidation', 'nature', 'perception', 'survival']}

    @property
    def equipment_selections(self):
        # [KEY[HowManySelections[ItemsAndQuantities]]]
        return {'choicesA': {1: {'great-axe': 1, 'martial-melee-weapon': 1}},
                'choicesB': {1: {'handaxe': 2, 'simple-weapon': 1}}}

    @property
    def starting_equipment(self):
        return {'explorers-pack': 1, 'javelins': 4}

    @property
    def sub_classes(self):
        return 'berserker'
