import player


class PlayerHandler():

    def __init__(self):
        self.players = {}
        self.playersbyname = {}
        self.unique_players = 0

    def add_player(self, player):
        if (not player.pid in self.players) and (not player.__full_name__() in self.playersbyname):
            self.players[player.pid] = player
            self.playersbyname[player.__full_name__()] = player
            self.unique_players += 1
        else:
            pass

        # if player.pid not in self.players:
        #     self.players[player.pid] = player # make sure that this creates a season on the player
        # else:
        #     # print("{} already seen, skipping\n".format(player.pid))
        #     # Don't want to skip, want to add new Season() to existing Player() inside self.players
        #     pass

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
        
    def printPlayersWithDuplicateSeasons(self):
        playersWithDupes = 0
        playersWithFRDupes = 0
        for player in self.players:
            if self.players[player].hasDuplicates:
                self.players[player].print_dup()
                if self.players[player].duplicateFreshman:
                    playersWithFRDupes+=1
                playersWithDupes += 1
        print("Num players w dupes: {}".format(playersWithDupes))
        print("Num players w freshman dupe: {}".format(playersWithFRDupes))


    def __players__(self):
        return self.players