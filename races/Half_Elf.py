from races.Race import Race


class HalfElf(Race):
    def __init__(self):
        super().__init__()
        self.score_modifiers['CHA'] += 2
        self.languages.append('elvish')

    def __str__(self):
        return 'Half-Elf'

    @property
    def size(self):
        return 'medium'

    @property
    def speed(self):
        return 30

    @property
    def age_range(self):
        return [20, 180]

    @property
    def traits(self):
        return ['darkvision', 'fey-ancestry', 'skill-versatility']

# TODO Half-Elf can select an additional Stat to add +1 for score modifiers, as well as
# TODO other selections regarding languages, proficiencies, etc