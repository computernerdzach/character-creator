from copy import copy
from random import randint


class Stats(object):
    keys = ['STR', 'DEX', 'INT', 'WIS', 'CHA', 'CON']

    def __init__(self):
        self.unassigned_rolls = self.roll_stats()
        self.unassigned_stats = copy(self.keys)
        self.STR = 0
        self.DEX = 0
        self.INT = 0
        self.WIS = 0
        self.CHA = 0
        self.CON = 0
        self.__state = {
            'STR': False,
            'DEX': False,
            'INT': False,
            'WIS': False,
            'CHA': False,
            'CON': False
        }

    def is_assigned(self, stat: str) -> bool:
        return self.__state[stat]

    def assign_stat(self, stat: str, value: int) -> None:
        setattr(self, stat, value)
        self.__state[stat] = True
        self.unassigned_stats.remove(stat)

    @staticmethod
    def roll_stats() -> list:
        i, j = 0, 0
        all_scores = list()
        while j < 6:
            scores = list()
            while i < 4:
                scores.append(randint(0, 6))
                i += 1
            scores.remove(min(scores))
            all_scores.append(sum(scores))
            j += 1
            i = 0
        return all_scores

    def assign_stats(self):
        done = False
        while not done:
            # ignore this warning
            indexed_stats = dict(list(enumerate(self.unassigned_stats)))
            indexed_roles = dict(list(enumerate(self.unassigned_rolls)))

            print(f'Here are your unassigned rolls:')
            for i, stat in indexed_roles.items():
                print(f'    {i}: {stat}')

            print(f'Here are your unassigned stats:')
            for k, label in indexed_stats.items():
                print(f'    {k}: {label}')

            user_stat = int(input('Which stat would you like to assign?\n-> '))
            roll_index = int(input('Which roll would you like to use?\n-> '))
            self.assign_stat(indexed_stats[user_stat], indexed_roles[roll_index])
            self.unassigned_rolls.remove(indexed_roles[roll_index])
            if len(self.unassigned_stats) == 0:
                done = True
