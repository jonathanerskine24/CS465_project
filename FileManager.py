import os.path as osp

COLLEGE_DATA_START = 2005
COLLEGE_DATA_END = 2013

NFL_DATA_START = None
NFL_DATA_END = None

class FileManager():




    def __init__(self):

        self.base_college_path = osp.join('data', 'college', '2005_2013')
        self.base_nfl_path = osp.join('data', 'nfl')

        self.college_season_files = self.__college_season_files__()


    def __college_season_files__(self):
        return  [ osp.join(self.base_college_path,str(year)) 
                   for year in range(COLLEGE_DATA_START, COLLEGE_DATA_END+1)
                ]


    def format_path(self, base_path):
        pass


        # file_path1 = osp.join('data', 'college', '2005_2013', '2009', 'player.csv')
        # file_path2 = osp.join('data', 'college', '2005_2013', '2009', 'player-game-statistics.csv')
