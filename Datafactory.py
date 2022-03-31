import csv
import json
import cfbd

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

        self.plays = {}
        self.players = {}
        self.altplayers = {}
        self.games = {}
        self.passes = {}
        self.rushes = {}
        self.receptions = {}

        self.initialize_cfbd()

        # self.load_players()
        # self.initialize_college_stats()
        # self.initialize_nfl_stats()
        # self.alt_nfl_setup()


    def initialize_cfbd(self):
        self.configure_API()
        self.cfdb = {}
        self.cfdb["teams"] = cfbd.TeamsApi(cfbd.ApiClient(self.configuration))
        self.cfdb["games"] = cfbd.GamesApi(cfbd.ApiClient(self.configuration))
        self.cfdb["plays"] = cfbd.PlaysApi(cfbd.ApiClient(self.configuration))

        # do something like
        # loop through each team, each week of each year and 
        # construct player data profiles this way

    def configure_API(self):
        # Configure API key authorization: ApiKeyAuth
        self.configuration = cfbd.Configuration()
        self.configuration.api_key['Authorization'] = 'Zvp+mqV+lEsjs5kuJ9qHAkvNxZEKZu6JpqqLktWq4gEvRi8sBIa+gpih6EY5BHLM'
        self.configuration.api_key_prefix['Authorization'] = 'Bearer'

    def initialize_nfl_stats(self):
        self.load_nfl_game_data()
    

    def initialize_college_stats(self):
        # for filename in self.fm.college_season_files:
            # with open(osp)
        pass

    def load_players(self):
        self.load_college_player_data()
        self.load_nfl_player_data()

    def load_college_player_data(self):
        for player_file in self.fm.__college_stat_files___("player.csv"):
            with open(player_file, "r") as f:
                reader = csv.reader(f)
                for p in reader:
                    if is_valid(p):
                        # print(p)
                        self.pHandler.add_college_player(pm.pack_college_player(p))
    
    def load_nfl_player_data(self):
        with open(self.fm.nfl_player_data_file, "r") as f:
            reader = csv.reader(f)
            lines = 0
            match = 0
            no_match = 0
            for p in reader:
                if (p[0] == p[6]):
                    match += 1
                else:
                    no_match += 1
                if (name_is("Tom Brady", p[1], p[2])):
                    print(p)
                # if (name_is("Percy Harvin", p[1], p[2])):
                #     print(p)
                self.pHandler.add_nfl_player(pm.pack_nfl_player(p))
                self.players[p[0]] = p
                self.altplayers[p[6]] = p
                lines += 1
            print("Match: {}, No Match: {}".format(match, no_match))


    # ok, wow, this is gonna be a behemoth of a function...
    def load_nfl_game_data(self):
        with open(self.fm.nfl_plays_data_file, "r") as f:
            print("\n\n")
            reader = csv.reader(f)
            for p in reader:
                self.plays[p[0]] = p
                
        with open(self.fm.nfl_game_data_file, "r") as f:
            print("\n\n")
            reader = csv.reader(f)
            for g in reader:
                self.games[g[0]] = g
                
        
        with open(self.fm.nfl_rusher_data_file, "r") as f:
            print("\n\n")
            reader = csv.reader(f)
            for r in reader:
                self.parse_rush(r)

    def parse_rush(self, r):
        play = self.plays[r[1]]
        game = self.games[play[1]]
        player = self.pHandler.get_nfl_player_name(r[3])
        if (player == -1):
            print("\n")
            print(self.altplayers[r[3]])
            print(r[3])
            player = "??"
        date = "{} {}".format(game[2], game[1])
        if (player == "??"):
            print("{}: {} rushes {} for {} yards".format(date, player, r[6], r[8]))


                
    def alt_nfl_setup(self):
        gamesdata = None
        playerprofs = None
        with open(self.fm.alt_nfl_games_file, "r") as f:
            gamesdata = json.load(f)
        
        with open(self.fm.alt_nfl_profiles_file, "r") as f:
            playerprofs = json.load(f)

        for i in playerprofs:
            if ("Dobbins" in i['name']):
                print(i)

        # print(playerprofs[0])
        # print("\n\n")
        # print(gamesdata[0])