from races.Race import Race


class Elf(Race):
    def __init__(self):
        super().__init__()
        self.score_modifiers['INT'] += 1
        self.languages.append('elvish')

    def __str__(self):
        return 'Elf'

    @property
    def size(self):
        return 'medium'

    @property
    def speed(self):
        return 30

    @property
    def age_range(self):
        return [100, 750]

    @property
    def traits(self):
        return ['darkvision', 'keen senses', 'fey ancenstry', 'trance']