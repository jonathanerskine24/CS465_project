import player


class PlayerHandler():

    def __init__(self):
        self.players = {}

    def addPlayer(self, player):
        if player.pid not in self.players:
            self.players[player.pid] = player # make sure that this creates a season on the player
        else:
            # print("{} already seen, skipping\n".format(player.pid))
            # Don't want to skip, want to add new Season() to existing Player() inside self.players
            pass

    def addSeasonToPlayer(self, playerID, season):
        self.players[playerID].addSeason(season)

    def addGameToPlayer(self, pid, game_data):
        # figure out how to determine season
        season = "FR"
        self.players[pid].addGame(season, game_data)

    def contains(self, pid):
        return (not (pid not in self.players))
            
    def getPlayer(self, player_id):
        return self.players[player_id]

    def printPlayers(self):
        for x in self.players:
            if (self.players[x].num_seasons_total > 2):
                self.players[x].print()
        
    def __players__(self):
        return self.players