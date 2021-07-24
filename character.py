from abc import ABC
from random import randint


# def roll_stats():
#     i, j = 0, 0
#     the_stats = list()
#     while i < 6:
#         each_stat = list()
#         while j < 4:
#             each_stat.append(randint(0, 6))
#             j += 1
#         small = min(each_stat)
#         each_stat.remove(small)
#         a_stat = sum(each_stat)
#         the_stats.append(a_stat)
#         i += 1
#         j = 0
#     return the_stats


# def assign_stats(self, stats):
#     skills = ['STR', 'DEX', 'INT', 'WIS', 'CHA', 'CON']
#     length = int(len(skills))
#     print("Please assign your stat scores:")
#     while length >= 1:
#         numbered_stats = enumerate(stats)
#         print("Stats:")
#         for j, every in numbered_stats:
#             print(f"({j} : {every})", end="")
#         print("")
#         print("Skills:")
#         for i, each in enumerate(skills):
#             print(f"({i} : {each}) ", end="")
#         print("")
#         score = int(input('Which score would you like to assign?'))
#         skill = int(input('Which skill would you like to apply it to?'))
#         if skills[skill] == 'STR':
#             self.STR = stats[score]
#             skills.remove(skills[skill])
#             stats.remove(stats[score])
#             length -= 1
#         elif skills[skill] == 'DEX':
#             self.DEX = stats[score]
#             skills.remove(skills[skill])
#             stats.remove(stats[score])
#             length -= 1
#         elif skills[skill] == 'INT':
#             self.INT = stats[score]
#             skills.remove(skills[skill])
#             stats.remove(stats[score])
#             length -= 1
#         elif skills[skill] == 'WIS':
#             self.WIS = stats[score]
#             skills.remove(skills[skill])
#             stats.remove(stats[score])
#             length -= 1
#         elif skills[skill] == 'CHA':
#             self.CHA = stats[score]
#             skills.remove(skills[skill])
#             stats.remove(stats[score])
#             length -= 1
#         elif skills[skill] == 'CON':
#             self.CON = stats[score]
#             skills.remove(skills[skill])
#             stats.remove(stats[score])
#             length -= 1
#         else:
#             print("Incorrect input, try again.")
#     print(f"str: {self.STR}, dex: {self.DEX}, int: {self.INT}, wis: {self.WIS}, cha: {self.CHA}, con: {self.CON}")


class Character(ABC):
    def __init__(self, name):
        self.name = name
        self.STR = 0
        self.DEX = 0
        self.INT = 0
        self.WIS = 0
        self.CHA = 0
        self.CON = 0

        # self.stats = roll_stats()
        # assign_stats(self, self.stats)

