import csv
from player_handler import PlayerHandler
from player import Player
from Stat_enums import Stat 
from FileManager import FileManager
from DataInfo import DataInfo as di
# would you pick a fuckin naming convention?

# kinda half assed these names, make better ones

from tests import *

from DataCleaningUtils import *

from Datafactory import DataFactory

import os.path as osp

phandler = PlayerHandler()
fm = FileManager()

'''
    Want to add players from every year, dealing with collisions to construct player profiles

'''

# first go through the player files to initialize players
#   consider:
#     - duplicates: how to handle? data authentication
#     - what is really happening when we "create" a player for each season? adding new seasons
#     - need to go season by season through player files initializing Player()s and 
#            adding to a Player_Manager()
#     - if player already exists, simply add a new season to the existing Player()


case_studies = [[],[]]
cs1 = "Anthony Pesanello"
cs2 = "Eli Tenuta"

unique_players = 0





# for year in di.COLLEGE_DATA_RANGE:
    # for file_type in fm.
    # print(fm.college_stat_files[year]['player.csv'])
    # print("Beginning {}...".format(year[-4:]))
    # with open(fm., "r") as f:
    #     reader = csv.reader(f)
    #     for p in reader:
    #         # print(p)
    #         if is_valid(p):
    #             # print("Valid\n")
    #             pid = p[0]
    #             # print(phandler.contains(pid))
    #             if (not phandler.contains(pid)):
    #                 unique_players+=1
    #                 if (name_is(cs1, p)):
    #                     p.append(year[-4:])
    #                     case_studies[0].append(p)
    #                 elif (name_is(cs2, p)):
    #                     p.append(year[-4:])
    #                     case_studies[1].append(p)
    #                 phandler.addPlayer(Player(p[3], p[2], p[6], p[0], p[1], p[5]))
    #             else:
    #                 if (name_is(cs1, p)):
    #                     p.append(year[-4:])
    #                     case_studies[0].append(p)
    #                 elif (name_is(cs2, p)):
    #                     case_studies[1].append(p)
    #                     p.append(year[-4:]) 
    #                 season = p[5]
    #                 phandler.addSeasonToPlayer(pid, p[5])
    #         else:
    #             print("Invalid, skipping {}\n".format(p))

# phandler.printPlayers()

df = DataFactory()

# phandler.printPlayersWithDuplicateSeasons()

print("Unique players: {}".format(df.pHandler.unique_players))
# for i in case_studies:
#     for x in i:
#         print(x)

# file_path1 = os.path.join('data', 'college', '2005_2013', '2009', 'player.csv')
# file_path2 = os.path.join('data', 'college', '2005_2013', '2009', 'player-game-statistics.csv')

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



