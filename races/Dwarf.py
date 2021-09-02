from races.Race import Race


class Dwarf(Race):
    def __init__(self):
        super().__init__()
        self.score_modifiers['CON'] += 2
        self.languages.append('dwarvish')

    def __str__(self):
        return 'Dwarf'

    @property
    def size(self):
        return 'medium'

    @property
    def speed(self):
        return 25

    @property
    def age_range(self):
        return [50, 350]

    @property
    def traits(self):
        return ['darkvision', 'dwarven-resilience', 'stonecunning', 'dwarven-combat-training', 'tool-proficiency']
