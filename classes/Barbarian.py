from classes.Char_Class import CharClass


class Barbarian(CharClass):
    # TODO: This should inherit from a parent class
    def __init__(self):

        super().__init__()

        self.hit_die = 12

        self.saving_throws['STR'] = self.proficiency_bonus + self.STR
        self.saving_throws['CON'] = self.proficiency_bonus + self.CON
        self.equipment = {'explorers-pack': 1, 'javelin': 4}
        self.proficiencies = list()

        self.pick_proficiencies()
        self.pick_equipment()

    def __str__(self):
        return 'Barbarian'

    @property
    def hit_die(self):
        return 12

    @property
    def tool_proficiencies(self):
        return 'light-armor', 'medium-armor', 'shields', 'simple-weapons', 'martial-weapons'

    @property
    def skill_proficiencies(self):
        return {'quantity': 2, 'choices': ('animal-handling', 'athletics', 'intimidation',
                                           'nature', 'perception', 'survival')}

    @property
    def saving_throw_assignment(self):
        return 'STR', 'CON'

    @property
    def starting_equipment_assignment(self):
        return {'explorers-pack': 1, 'javelins': 4}

    @property
    def sub_classes(self):
        return 'berserker'

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

    def assign_savingthrows(self):
        for each in self.saving_throws:
            if each in self.saving_throw_assignment():
                thing = self.saving_throw_switch(self, each)
                thing += (self.STR / 2) + self.proficiency_bonus

        # for each in self.saving_throw_assignment():
        # if each == 'STR':
        #     self.saving_throws[each] += ((self.STR/2) + self.proficiency_bonus)
        # elif each ==

    def saving_throw_switch(self, save):
        switch = {
            'STR': self.STR,
            'DEX': self.DEX,
            'INT': self.INT,
            'WIS': self.WIS,
            'CHA': self.CHA,
            'CON': self.CON,
        }
        return switch.get(save, "Invalid input")
