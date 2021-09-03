from abc import ABC, abstractmethod


class CharClass(ABC):
    def __init__(self):

        self.proficiency_bonus = 2

    @property
    @abstractmethod
    def hit_die(self):
        pass

    @property
    @abstractmethod
    def tool_proficiencies(self):
        pass

    @property
    @abstractmethod
    def starting_equipment(self):
        pass

    @property
    @abstractmethod
    def sub_classes(self):
        pass

    @property
    @abstractmethod
    def saving_throws(self) -> list:
        pass

    @property
    @abstractmethod
    def proficiency_selections(self) -> list:
        pass

    @staticmethod
    def pick_proficiencies(proficiency_options):
        # how many proficiencies you can select
        pro_amount = next(iter(proficiency_options))

        # the options you can choose from
        options = proficiency_options[pro_amount]

        print(f"Please select {pro_amount} proficiencies.")

        # set up loop
        i = 0
        selections = list()

        # while there are selections left to make...
        while i < pro_amount:
            # print out available choices with index
            for j, each in enumerate(options):
                print(f"{j}: {each}")

            # user enters choice
            choice = int(input('Selection: '))
            # choice is added to character
            selections += options[choice]
            # choice is removed from selectable items and iterate count
            options.remove(options[choice])
            i += 1

        # return a list of proficiency selections
        return selections

    @staticmethod
    def pick_equipment(selections, starting):
        returnable = starting
        for collection in selections:

            choice_quant = next(iter(selections[collection]))
            i = 0
            while i < choice_quant:
                print(f'Please select {choice_quant} pieces of equipment.')
                the_list = selections[collection][choice_quant]
                items = []
                for j, equipment in enumerate(the_list):
                    print(f'{j}: {equipment} x {the_list[equipment]}')
                    items.append(equipment)
                user_select = int(input('-> '))
                user_select = items[user_select]

                returnable[user_select] = the_list[user_select]
                i += 1

        return returnable



        # amount_a, amount_b = 1, 1
        # a, b = 0, 0
        # # choices_a = {'great-axe': 1, 'martial-melee-weapon': 1}
        # # choices_b = {'handaxe': 2, 'simple-weapon': 1}
        # print(f"Please select {amount_a} pieces of equipment from list A and {amount_b} pieces of equipment from "
        #       f"list B:")
        # list_a, list_b = [], []
        # while a < amount_a:
        #     print("List A:")
        #     for i, each in enumerate(choices_a):
        #         print(f"{i}: {each}")
        #         list_a.append(each)
        #     choice_a = int(input("List A selection: "))
        #     name_a = list_a[choice_a]
        #     key_a = choices_a[name_a]
        #     returnable[name_a] = key_a
        #     a += 1
        # while b < amount_b:
        #     print("List B:")
        #     for i, each in enumerate(choices_b):
        #         print(f"{i}: {each}")
        #         list_b.append(each)
        #     choice_b = int(input("List B selection: "))
        #     name_b = list_b[choice_b]
        #     key_b = choices_b[name_b]
        #     returnable[name_b] = key_b
        #     b += 1
        # return returnable