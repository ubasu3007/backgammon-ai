from src.strategies import Strategy
from src.piece import Piece
from src.compare_all_moves_strategy import CompareAllMoves

#weights was provided through a driver function 

class player1_11987797(CompareAllMoves):


            # 'number_occupied_spaces': number_occupied_spaces,
            # 'opponents_taken_pieces': opponents_taken_pieces,
            # 'sum_distances': sum_distances,
            # 'sum_distances_opponent': sum_distances_opponent,
            # 'number_of_singles': number_of_singles,
            # 'sum_single_distance_away_from_home': sum_single_distance_away_from_home,
            # 'pieces_on_board': pieces_on_board,
            # 'sum_distances_to_endzone': sum_distances_to_endzone,
    def __init__(self, weights):
        self.weights = weights

    def evaluate_board(self, myboard, colour):
        board_stats = self.assess_board(colour, myboard)

        board_value = (2)*board_stats['sum_distances'] + (2)*board_stats['number_of_singles'] + \
                      (-2)*board_stats['number_occupied_spaces'] + (-1)*board_stats['opponents_taken_pieces'] + \
                      (-1.5)*board_stats['sum_distances_opponent'] + (2)*board_stats['sum_single_distance_away_from_home']+\
                      (3)*board_stats['pieces_on_board'] + (1)*board_stats['sum_distances_to_endzone']
        return board_value

class player2_11987797(CompareAllMoves):

    def __init__(self, weights):
        self.weights = weights


              # 'NOVEL_FEATURE': novel_feature_value,
            # 'number_occupied_spaces': number_occupied_spaces,
            # 'opponents_taken_pieces': opponents_taken_pieces,
            # 'sum_distances': sum_distances,
            # 'sum_distances_opponent': sum_distances_opponent,
            # 'number_of_singles': number_of_singles,
            # 'sum_single_distance_away_from_home': sum_single_distance_away_from_home,
            # 'pieces_on_board': pieces_on_board,
            # 'sum_distances_to_endzone': sum_distances_to_endzone,


    def evaluate_board(self, myboard, colour):
        board_stats = self.assess_board(colour, myboard)

        board_value = (2)*board_stats['sum_distances'] + (2)*board_stats['number_of_singles'] + \
                      (-2)*board_stats['number_occupied_spaces'] + (-1)*board_stats['opponents_taken_pieces'] + \
                      (-1.5)*board_stats['sum_distances_opponent'] + (2)*board_stats['sum_single_distance_away_from_home']+\
                      (3)*board_stats['pieces_on_board'] + (1)*board_stats['sum_distances_to_endzone'] + \
                        (-2)*board_stats['opponent_number_singles']
        # board_value = board_stats[NOVEL_FEATURE] * 2 + board_stats['sum_distances'] + 2 * board_stats['number_of_singles'] - \
        #               board_stats['number_occupied_spaces'] - board_stats['opponents_taken_pieces']
        return board_value