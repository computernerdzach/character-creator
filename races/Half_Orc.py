from races.Race import Race


class HalfOrc(Race):
    def __init__(self):
        super().__init__()
        self.score_modifiers['STR'] += 2
        self.score_modifiers['CON'] += 1
        self.languages.append('orc')

    def __str__(self):
        return 'Half-Orc'

    @property
    def size(self):
        return 'medium'

    @property
    def speed(self):
        return 30

    @property
    def age_range(self):
        return [14, 75]

    @property
    def traits(self):
        return ['darkvision', 'savage-attacks', 'relentless-endurance']
