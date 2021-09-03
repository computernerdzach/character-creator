from races.Race import Race


class Dragonborn(Race):

    def __init__(self):
        super().__init__()
        self.score_modifiers['STR'] = 2
        self.score_modifiers['CHA'] = 1
        self.languages.append('draconic')

    def __str__(self):
        return 'Dragonborn'

    @property
    def size(self):
        return 'medium'

    @property
    def speed(self):
        return 30

    @property
    def age_range(self):
        return [15, 80]

    @property
    def traits(self):
        return ['draconic-ancestry', 'breath-weapon', 'damage-resistance']
