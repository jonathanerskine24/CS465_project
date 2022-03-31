class DataInfo():
    COLLEGE_DATA_BEGIN = 2005
    COLLEGE_DATA_END = 2013
    NFL_DATA_BEGIN = 1940
    NFL_DATA_END = 2022
    
    COLLEGE_DATA_RANGE = [str(y) for y in range(COLLEGE_DATA_BEGIN, COLLEGE_DATA_END+1)]

    INVALID_ENTRIES = ["Player_Code", "Player Code"]
