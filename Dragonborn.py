import race


class Dragonborn(race.Race):
    def __init__(self, name, a_race, hp_bonus, hit_points):
        super().__init__(self, name, a_race)
        self.hp_bonus = hp_bonus
        self.hit_points = hit_points
