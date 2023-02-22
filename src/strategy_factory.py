from src.compare_all_moves_strategy import CompareAllMovesSimple, \
    CompareAllMovesWeightingDistanceAndSingles, \
        CompareAllMovesWeightingDistanceAndSinglesWithEndGame, \
            CompareAllMovesWeightingDistance
from src.strategies import MoveFurthestBackStrategy, HumanStrategy, MoveRandomPiece
from src.anderson import player1_anderson,player2_anderson



class StrategyFactory:
    @staticmethod
    def create_by_name(strategy_name):
        for strategy in StrategyFactory.get_all():
            if strategy.__name__ == strategy_name:
                return strategy()

        raise Exception("Cannot find strategy %s" % strategy_name)

    @staticmethod
    def get_all():
        strategies = [
            MoveRandomPiece,
            MoveFurthestBackStrategy,
            CompareAllMovesSimple,
            player1_anderson,
            player2_anderson,
            CompareAllMovesWeightingDistanceAndSinglesWithEndGame,
            CompareAllMovesWeightingDistanceAndSingles,
            CompareAllMovesWeightingDistance,
            HumanStrategy,
        ]
        return strategies
