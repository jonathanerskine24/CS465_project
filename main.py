import csv
from player_handler import PlayerHandler
from player import Player
from Stat_enums import Stat

phandler = PlayerHandler()

with open("data/college/2005_2013/2009/player.csv", "r") as f:
    reader = csv.reader(f)
    for p in reader:
        phandler.addPlayer(Player(p[3], p[2], p[6], p[0], p[1]))
        
with open("data/college/2005_2013/2009/player-game-statistics.csv", "r") as f:
    reader = csv.reader(f)
    for g in reader:
        if g[0] != 'Player Code':
            phandler.addGameToPlayer(g[0], g[1:19])

phandler.printPlayers()

