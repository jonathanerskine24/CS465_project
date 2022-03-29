from game_stats import Game_Stats
from season import Season

class Player():

    def __init__(self, fname, lname, pos, pid, school):
        self.first_name = fname
        self.last_name = lname
        self.position = pos
        self.pid = pid
        self.school = school
        self.seasons = {'FR':None, 'SO':None, 'JR':None, 'SR':None}

    def addGame(self, season, gamedata):
        if self.seasons[season] is None:
            self.seasons[season] = Season()
        self.seasons[season].add_game(gamedata)

    def print(self):
        print(self.get_readable())

    def get_readable(self):
        return "{} {} {} {} {}".format(self.first_name, self.last_name, self.position, self.pid, self.school) 
        