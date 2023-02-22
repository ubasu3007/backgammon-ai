import json

from src.board import Board
from src.colour import Colour
from src.strategy_factory import StrategyFactory

if __name__ == '__main__':
    s = input('Paste move info:\n')
    data = json.loads(s)

    strategy = StrategyFactory.create_by_name(data['strategy'])

    board = Board()
    for location, value in data['board'].items():
        board.add_many_pieces(value['count'], Colour.load(value['colour']), int(location))

    strategy.move(
        board=board,
        colour=Colour.load(data['colour_to_move']),
        dice_roll=data['dice_roll'],
        make_move=lambda l, r: board.move_piece(board.get_piece_at(l), r),
        opponents_activity={})

    board.print_board()
