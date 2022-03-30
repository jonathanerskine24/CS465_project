from Stat_enums import Stat

def pack(gamedata):
    return {
        stat.name: gamedata[stat.value] 
            for stat in Stat.__iter__()
    }

def pack_tester(gamedata):
    ret = {}
    for i in range(0, len(gamedata)):
        ret[Stat._value2member_map_[i].name] = gamedata[i]
    return ret
