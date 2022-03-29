from Stat_enums import Stat

class Season():

    def __init__(self):
        self.games = []
        self.total_data = []

    def add_game(self, game):
        self.games.append(game)