import race


class Dragonborn(race.Race):

    def __init__(self, name):
        super().__init__(name)

    @property
    def size(self):
        return 'medium'
