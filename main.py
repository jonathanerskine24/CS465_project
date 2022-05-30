import csv
from player_handler import PlayerHandler
from player import Player
from Stat_enums import Stat 
from FileManager import FileManager
from DataInfo import DataInfo as di

import cfbd
from tests import *
from DataCleaningUtils import *
from Datafactory import DataFactory
import os.path as osp

phandler = PlayerHandler()
fm = FileManager()

df = DataFactory()


plays2017 = df.cfdb['plays'].get_play_stats(year=2017, week=2, team="Alabama")
print(plays2017[0])
plays2018 = df.cfdb['plays'].get_play_stats(year=2018, week=2, team='Alabama')
print("\n")
print(plays2018[0])
print("{} {}".format(len(plays2017), len(plays2018)))

# for team in teams:
    # print(team)
    # print(df.cfdb['teams'].get_roster(team=team.school, year=56))

# print(teams[103].school)


# print("Unique college players: {}".format(df.pHandler.unique_college_players))
# print("Unique NFL players: {}".format(df.pHandler.unique_nfl_players))





# with open(file_path1, "r") as f:
#     reader = csv.reader(f)
#     for p in reader:
#         phandler.addPlayer(Player(p[3], p[2], p[6], p[0], p[1]))
        
# game_data = None

# with open(file_path2, "r") as f:
#     reader = csv.reader(f)
#     for g in reader:
#         if g[0] != 'Player Code':
#             game_data = g[1:20]
#             phandler.addGameToPlayer(g[0], g[1:20])

# fm = FileManager()

# # fp3 = os.path.join(file_path1, "extension")
# # print(fp3)



