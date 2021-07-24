from races.Race import Race


class Halfling(Race):
    def __init__(self):
        super().__init__()
        self.score_modifiers['DEX'] += 2
        self.languages.append('halfling')

    def __str__(self):
        return 'Halfling'

    @property
    def size(self):
        return 'small'

    @property
    def speed(self):
        return 25

    @property
    def age_range(self):
        return [20, 250]

    @property
    def traits(self):
        return ['brave', 'halfling-nimbleness', 'lucky']
