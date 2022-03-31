import os.path as osp
from DataInfo import DataInfo as di

class FileManager():




    def __init__(self):

        self.base_college_path = osp.join('data', 'college', '2005_2013')
        self.base_nfl_path = osp.join('data', 'nfl')

        self.college_stat_files = ["player.csv", "player-game-statistics.csv"]

        self.college_season_directories = self.__college_season_files__()
        self.college_stat_files_dict = self.__college_stat_files_dict__()

        self.nfl_player_data_file = osp.join(self.base_nfl_path, 'players.csv')
 

    def __college_season_files__(self):
        return  { year: osp.join(self.base_college_path,year) 
                    for year in di.COLLEGE_DATA_RANGE
        }

    def __college_stat_files_dict__(self):
        return {
            year: {stat: self.gen_file_name(year, stat) 
                for stat in self.college_stat_files }
            for year in di.COLLEGE_DATA_RANGE
        }

    def __college_stat_files___(self, stat):
        if (stat is None):
            return self.college_stat_files_dict

        return [
            self.college_stat_files_dict[year][stat] for year in di.COLLEGE_DATA_RANGE
        ]
        
    def gen_file_name(self, year, fn):
        return osp.join(self.college_season_directories[year], fn)

    def format_path(self, base_path):
        pass



        # file_path1 = osp.join('data', 'college', '2005_2013', '2009', 'player.csv')
        # file_path2 = osp.join('data', 'college', '2005_2013', '2009', 'player-game-statistics.csv')
