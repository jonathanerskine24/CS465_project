import csv

from FileManager import FileManager
from player_handler import PlayerHandler

from Stat_enums import Stat

from PackMan import PackMan as pm
from DataCleaningUtils import *

import os.path as osp

from DataInfo import DataInfo as di


class DataFactory():

    def __init__(self):

        self.pHandler = PlayerHandler()
        self.fm = FileManager()

        self.initialize_college_stats()
        self.initialize_nfl_stats()
        


    def initialize_nfl_stats(self):
        pass

    def initialize_college_stats(self):
        # for filename in self.fm.college_season_files:
            # with open(osp)

        self.load_players()
        pass

    def load_players(self,):
        self.load_college_player_data()
        self.load_nfl_player_data()

    def load_college_player_data(self):
        for player_file in self.fm.__college_stat_files___("player.csv"):
            with open(player_file, "r") as f:
                reader = csv.reader(f)
                for p in reader:
                    if is_valid(p):
                        # print(p)
                        self.pHandler.add_player(pm.pack_college_player(p))
    
    def load_nfl_player_data(self):
        with open(self.fm.nfl_player_data_file, "r") as f:
            reader = csv.reader(f)
            lines = 0
            for p in reader:
                # if (name_is("Tom Brady", p[1], p[2])):
                    # print(p)
                # if (name_is("Percy Harvin", p[1], p[2])):
                #     print(p)
                # self.pHandler.add_player(pm.pack_nfl_player(p))
                lines += 1
                # print(p)

