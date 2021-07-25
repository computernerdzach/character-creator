from races.Race import Race


class Gnome(Race):
    def __init__(self):
        super().__init__()
        self.score_modifiers['INT'] += 2
        self.languages.append('gnomish')

    def __str__(self):
        return 'Gnome'

    @property
    def size(self):
        return 'small'

    @property
    def speed(self):
        return 25

    @property
    def age_range(self):
        return [40, 500]

    @property
    def traits(self):
        return ['darkvision', 'gnome -cunning']
