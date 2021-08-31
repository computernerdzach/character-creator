from classes.CharClass import CharClass


class Barbarian(CharClass):
    # TODO: This should inherit from a parent class
    def __init__(self):

        super().__init__()

        self.proficiencies = self.pick_proficiencies(self)
        self.equipment = self.pick_equipment(self)

    def __str__(self):
        return 'Barbarian'

    @property
    def hit_die(self):
        return 12

    @property
    def tool_proficiencies(self):
        return 'light-armor', 'medium-armor', 'shields', 'simple-weapons', 'martial-weapons'

    @property
    def saving_throws(self):
        return 'STR', 'CON'

    @property
    def starting_equipment(self):
        return {'explorers-pack': 1, 'javelins': 4}

    @property
    def sub_classes(self):
        return 'berserker'

    @staticmethod
    def pick_proficiencies(self):
        pro_amount = 2
        proficiency_options = ['animal-handling', 'athletics', 'intimidation', 'nature', 'perception', 'survival']
        print(f"Please select {pro_amount} proficiencies.")
        i = 0
        selections = list()
        while i < pro_amount:
            for j, each in enumerate(proficiency_options):
                print(f"{j}: {each}")
            choice = int(input('Selection: '))
            selections += proficiency_options[choice]
            # self.proficiencies.append(proficiency_options[choice])
            proficiency_options.remove(proficiency_options[choice])
            i += 1
        return selections

    @staticmethod
    def pick_equipment(self):
        returnable = dict()
        returnable["explorers-pack"] = 1
        returnable["javelin"] = 4
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
            returnable[name_a] = key_a
            a += 1
        while b < amount_b:
            print("List B:")
            for i, each in enumerate(choices_b):
                print(f"{i}: {each}")
                list_b.append(each)
            choice_b = int(input("List B selection: "))
            name_b = list_b[choice_b]
            key_b = choices_b[name_b]
            returnable[name_b] = key_b
            b += 1
        return returnable
