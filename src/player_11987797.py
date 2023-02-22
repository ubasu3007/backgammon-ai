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

        board_value = self.weights[0]*board_stats['sum_distances'] + self.weights[1]*board_stats['number_of_singles'] + \
                      self.weights[2]*board_stats['number_occupied_spaces'] + self.weights[3]*board_stats['opponents_taken_pieces'] + \
                      self.weights[4]*board_stats['sum_distances_opponent'] + self.weights[5]*board_stats['sum_single_distance_away_from_home']+\
                      self.weights[6]*board_stats['pieces_on_board'] + self.weights[7]*board_stats['sum_distances_to_endzone']
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

        board_value = self.weights[0]*board_stats['sum_distances'] + self.weights[1]*board_stats['number_of_singles'] + \
                      self.weights[2]*board_stats['number_occupied_spaces'] + self.weights[3]*board_stats['opponents_taken_pieces'] + \
                      self.weights[4]*board_stats['sum_distances_opponent'] + self.weights[5]*board_stats['sum_single_distance_away_from_home']+\
                      self.weights[6]*board_stats['pieces_on_board'] + self.weights[7]*board_stats['sum_distances_to_endzone'] + \
                        self.weights[8]*board_stats['opponent_number_singles']
        # board_value = board_stats[NOVEL_FEATURE] * 2 + board_stats['sum_distances'] + 2 * board_stats['number_of_singles'] - \
        #               board_stats['number_occupied_spaces'] - board_stats['opponents_taken_pieces']
        return board_value