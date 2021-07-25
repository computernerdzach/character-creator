from races.Race import Race


class Human(Race):
    def __init__(self):
        super().__init__()
        self.score_modifiers['CHA'] += 1
        self.score_modifiers['STR'] += 1
        self.score_modifiers['WIS'] += 1
        self.score_modifiers['INT'] += 1
        self.score_modifiers['CON'] += 1
        self.score_modifiers['DEX'] += 1
        # self.languages.append('') TODO select from list of languages

    def __str__(self):
        return 'Human'

    @property
    def size(self):
        return 'medium'

    @property
    def speed(self):
        return 30

    @property
    def age_range(self):
        return [16, 90]

    @property
    def traits(self):
        pass
        # TODO humans have no traits?