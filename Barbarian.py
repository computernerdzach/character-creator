import Dragonborn


class Barbarian(Dragonborn.Dragonborn):

    def __init__(self, char_obj):
        super().__init__(char_obj)
        self.pro_choices = list()

        pro_amount = 2
        proficiencies = ['animal-handling', 'athletics', 'intimidation', 'nature', 'perception', 'survival']
        print(f"Please select {pro_amount} proficiencies.")
        i = 0
        while i < pro_amount:
            for j, each in enumerate(proficiencies):
                print(f"{j}: {each}")
            choice = int(input('Selection: '))
            self.pro_choices.append(proficiencies[choice])
            proficiencies.remove(proficiencies[choice])
            i += 1

    @property
    def hit_die(self):
        return 12

    @property
    def tool_proficiencies(self):
        return 'light-armor', 'medium-armor', 'shields', 'simple-weapons', 'martial-weapons'

    @property
    def prof_choices(self):
        return pro_choices

    # @property
    # def proficiency_choices(self):
    #
    #     return pro_choices
