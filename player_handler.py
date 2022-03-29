import player


class PlayerHandler():

    def __init__(self):
        self.players = {}

    def addPlayer(self, player):
        if player.pid not in self.players:
            self.players[player.pid] = player
        else:
            print("{} already seen, skipping\n".format(player.pid))

    def addGameToPlayer(self, pid, game_data):
        # figure out how to determine season
        season = "FR"
        self.players[pid].addGame(season, game_data)

    def getPlayer(self, player_id):
        return self.players[player_id]

    def printPlayers(self):
        for x in self.players:
            self.players[x].print()
            