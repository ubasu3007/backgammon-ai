# Play backgammon
from src.compare_all_moves_strategy import CompareAllMovesWeightingDistance, CompareAllMovesWeightingDistanceAndSingles
from src.experiment import Experiment
from src.strategies import MoveFurthestBackStrategy
from src.compare_all_moves_strategy import CompareAllMovesWeightingDistance
from src.anderson import player1_anderson, player2_anderson
from src.player_11987797 import player1_11987797, player2_11987797
from scipy.optimize import minimize
import numpy as np


def tester(weights):
    player = player1_11987797(weights)
    experiment = Experiment(
        games_to_play=100,
        white_strategy=player,
        black_strategy=MoveFurthestBackStrategy()
    )
    if __name__ == '__main__':
        experiment.run()
        experiment.print_results()
    white_wins = experiment.get_white_wins()
    return white_wins

print(tester([2, 2, -2, -1, -1.5, 2, 3, 1]))


#initial_guess = [2, 2, -2, 0, -1.5, 0, 0, 0.5]

#result = minimize(tester, initial_guess)
#print("Weights:", result) 


# Null hypothesis is that the strategies equally good
# Define a joint event of a random coin toss to determine who starts followed by a game,
# Under the null hypothesis, for a single event, p(win) = 0.5
# Assuming the strategies are equal (null hypothesis): P(n_wins) = binom(n_wins, n_games, 0.5)
