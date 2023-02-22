from random import randint

from src.colour import Colour
from src.game import Game
from src.strategy_factory import StrategyFactory
from src.strategies import HumanStrategy

if __name__ == '__main__':
    name = input('What is your name?\n')

    print("Available Strategies:")
    strategies = [x for x in StrategyFactory.get_all() if x.__name__ != HumanStrategy.__name__]
    for i, strategy in enumerate(strategies):
        print("[%d] %s (%s)" % (i, strategy.__name__, strategy.get_difficulty()))

    strategy_index = int(input('Pick a strategy:\n'))

    chosen_strategy = StrategyFactory.create_by_name(strategies[strategy_index].__name__)

    game = Game(
        white_strategy=HumanStrategy(name),
        black_strategy=chosen_strategy,
        first_player=Colour(randint(0, 1))
    )

    game.run_game(verbose=False)

    print("%s won!" % game.who_won())
    game.board.print_board()
