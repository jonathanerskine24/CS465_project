from game_stats import Game_Stats
from season import Season
import enum

COLLEGE_SEASONS = ["FR", "SO", "JR", "SR"]
YEAR = {"FR":0, "SO":1, "JR":2, "SR":3}

# class YEAR(enum.Enum):
#     FR=0
#     SO=1
#     JR=2
#     SR=3

# Perhaps "Base_Player" for common positions
class Player():

    def __init__(self, fname, lname, pos, pid, school, year):
        self.first_name = fname
        self.last_name = lname
        self.position = pos
        self.pid = pid
        self.school = school

        self.num_college_seasons = 0       # Something fucky going on with how this is getting incremented... 
        self.num_pro_seasons = 0            # some players have 3 seasons listed and a 3, some have a 4...
        self.num_seasons_total = 0

        self.college_seasons_counts = [0,0,0,0]

        # Convention: 'FR', 'SO', 'JR', 'SR', 'ROOKIE', '2', '3' ... 
        self.seasons = {'FR':None, 'SO':None, 'JR':None, 'SR':None}

        if year in COLLEGE_SEASONS:
            self.init_college(year)
        else:
            self.init_nfl()

        self.hasDuplicates = False
        self.duplicateFreshman = False


    # determine a convention for adding a game to a player
    # considerations:
    #       - what format is the data coming in? what do I have, what do I need/want?
    #       - might want to create a separate "Game" class... look for more data sets

    def init_college(self, year):
            self.seasons[year] = Season()
            self.college_seasons_counts[YEAR[year]] += 1
            self.num_college_seasons += 1
            self.num_seasons_total += 1

    def init_nfl(self):
        pass

    def addGame(self, season, gamedata):
        if self.seasons[season] is None:
            self.seasons[season] = Season()
        self.seasons[season].add_game(gamedata)

    def addSeason(self, season):
        self.seasons[season] = Season()
        self.num_seasons_total += 1
        if (season in COLLEGE_SEASONS):
            self.num_college_seasons += 1
            self.college_seasons_counts[YEAR[season]] += 1
            if (self.college_seasons_counts[YEAR[season]] > 1):
                if (season == "FR"):
                    self.duplicateFreshman = True
                self.hasDuplicates = True
        else:
            self.num_pro_seasons += 1

    def seasons_found(self):
        ret = ""
        for key in self.seasons:
            if (not self.seasons[key] is None):
                ret += (key +", ")
        return ret[:-2]

    def __full_name__(self):
        return (self.first_name + " " + self.last_name)

    def print(self):
        print(self.get_name() + " {} {} ".format(self.position, self.pid))

    def print_dup(self):
        print(self.get_name() + " FR:{}/SO:{}/JR:{}/SR:{}".format(self.college_seasons_counts[0],self.college_seasons_counts[1],self.college_seasons_counts[2],self.college_seasons_counts[3]))

    def get_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_readable(self):
        return "{} {} {} {} {}".format(self.first_name, self.last_name, self.position, self.pid, self.school) 


# figure out how to abstract this
class CollegePlayer(Player):
    pass

class NFLPlayer(Player):
    pass


# finally "Player" - highest level interface
# comprised of both CollegePlayer and NFLPlayer ... but what does this solve?
# perhaps nothing. Might be better off with single Player class to handle both.