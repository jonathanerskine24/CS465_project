from DataCleaningUtils import *

def test_pack(game_data):
    if (pack(game_data) != pack_tester(game_data)):
        return False
    else:
        return True


    # print("Game Data:")
    # print(game_data)

    # print("\n\nGame Data 1:")
    # print(pack(game_data))

    # # print(Stat._value2member_map_[0])
    # print("\nGame Data 2:")
    # print(pack2(game_data))