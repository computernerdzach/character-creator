import Dragonborn


class Barbarian(Dragonborn.Dragonborn):

    def __init__(self, char_obj):
        super().__init__(char_obj)

        self.saving_throws = ['STR', 'CON']
        self.equipment = {}
        self.proficiencies = list()

        self.pick_proficiencies()
        self.pick_equipment()

    @property
    def hit_die(self):
        return 12

    @property
    def tool_proficiencies(self):
        return 'light-armor', 'medium-armor', 'shields', 'simple-weapons', 'martial-weapons'

    def pick_proficiencies(self):
        pro_amount = 2
        proficiency_options = ['animal-handling', 'athletics', 'intimidation', 'nature', 'perception', 'survival']
        print(f"Please select {pro_amount} proficiencies.")
        i = 0
        while i < pro_amount:
            for j, each in enumerate(proficiency_options):
                print(f"{j}: {each}")
            choice = int(input('Selection: '))
            self.proficiencies.append(proficiency_options[choice])
            proficiency_options.remove(proficiency_options[choice])
            i += 1

    def pick_equipment(self):
        self.equipment["explorers-pack"] = 1
        self.equipment["javelin"] = 4
        amount_a, amount_b = 1, 1
        a, b = 0, 0
        choices_a = {'great-axe': 1, 'martial-melee-weapon': 1}
        choices_b = {'handaxe': 2, 'simple-weapon': 1}
        print(f"Please select {amount_a} pieces of equipment from list A and {amount_b} pieces of equipment from "
              f"list B:")
        list_a, list_b = [], []
        while a < amount_a:
            print("List A:")
            for i, each in enumerate(choices_a):
                print(f"{i}: {each}")
                list_a.append(each)
            choice_a = int(input("List A selection: "))
            name_a = list_a[choice_a]
            key_a = choices_a[name_a]
            self.equipment[name_a] = key_a
            a += 1
        while b < amount_b:
            print("List B:")
            for i, each in enumerate(choices_b):
                print(f"{i}: {each}")
                list_b.append(each)
            choice_b = int(input("List B selection: "))
            name_b = list_b[choice_b]
            key_b = choices_b[name_b]
            self.equipment[name_b] = key_b
            b += 1
