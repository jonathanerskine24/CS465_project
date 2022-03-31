from Stat_enums import Stat

from DataInfo import DataInfo as di

from player import Player



def all_data_present(p):
    for i in p[0:6]:
        if (i == ""):
            return False
    return True
    
def is_valid(p):
    return (p[0] not in di.INVALID_ENTRIES) and (p[2] != "Team") and (all_data_present(p))

def name_is(name, fn, ln):
    return (name.split(' ') == [fn, ln])






# class PackMan():

#     @classmethod
#     def pack_college_player(p):
#         return Player(p[3], p[2], p[6], p[0], p[1], p[5])
    
#     @classmethod
#     def pack_game_data(gamedata):
#         return {
#             stat.name: gamedata[stat.value] 
#                 for stat in Stat.__iter__()
#         }