from Stat_enums import Stat

from DataInfo import DataInfo as di

from player import Player

'''
    Player(fname, lname, pos, pid, school, year)

'''

class PackMan(object):

    @staticmethod
    def pack_college_player(p):
        return Player(p[3], p[2], p[6], p[0], p[1], p[5])

    @staticmethod
    def pack_nfl_player(p):
        return Player(p[1], p[2], p[4], p[0], p[8], "NFL")
        # return Player(p?)
    
    @classmethod
    def pack_game_data(gamedata):
        return {
            stat.name: gamedata[stat.value] 
                for stat in Stat.__iter__()
        }
    