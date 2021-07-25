from races.Race import Race


class Tiefling(Race):

    def __init__(self):
        super().__init__()
        self.score_modifiers['CHA'] += 2
        self.score_modifiers['INT'] += 1
        self.languages.append('abyssal')

    def __str__(self):
        return 'Tiefling'

    @property
    def size(self):
        return 'medium'

    @property
    def speed(self):
        return 30

    @property
    def age_range(self):
        return [16, 100]

    @property
    def traits(self):
        return ['darkvision', 'hellish-resistance', 'infernal-legacy']
