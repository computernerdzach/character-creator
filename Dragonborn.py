import character


class Dragonborn(character.Character):

    def __init__(self, name):
        super().__init__(name)
        self.STR += 2
        self.CHA += 1

    @property
    def size(self):
        return 'medium'

    @property
    def speed(self):
        return 30

    @property
    def age_range(self):
        return 15, 80

    @property
    def languages(self):
        return 'common', 'draconic'

    @property
    def traits(self):
        return 'draconic-ancestry', 'breath-weapon', 'damage-resistance'
