import csv
from player_handler import PlayerHandler
from player import Player
from Stat_enums import Stat 
from FileManager import FileManager
# would you pick a fuckin naming convention?

# kinda half assed these names, make better ones
from data_manip import *
from tests import *

import os.path as osp

phandler = PlayerHandler()
fm = FileManager()

'''
    Want to add players from every year, dealing with collisions to construct player profiles

    

'''

# first go through the player files to initialize players
#   consider:
#     - duplicates: how to handle? 
#     - what is really happening when we "create" a player for each season? adding new seasons
#     - need to go season by season through player files initializing Player()s and 
#            adding to a Player_Manager()
#     - if player already exists, simply add a new season to the existing Player()

for year in fm.college_season_files:
    print("Beginning {}...".format(year))
    with open(osp.join(year, 'player.csv'), "r") as f:
        reader = csv.reader(f)
        for p in reader:
            if p[0] != 'Player_Code':
                pid = p[0]
                # print(phandler.contains(pid))
                if (not phandler.contains(pid)):
                    phandler.addPlayer(Player(p[3], p[2], p[6], p[0], p[1], p[5]))
                else:
                    season = p[5]
                    phandler.addSeasonToPlayer(pid, p[5])

phandler.printPlayers()


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



