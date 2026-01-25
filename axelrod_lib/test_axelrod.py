import axelrod
from core.match_history import match_history, score, match_history_with_noise
import inspect
import axelrod as axl
from simulation import round_robin

"""
This file enables use of the official strategies in the axelrod library in this project.
"""


def match_axl(player1, player2, rounds, noise=0):
    """"Play a match between two Axelrod strategies and return the match history as a list of tuples of booleans (adapted for functions in our project)."""
    match = axl.Match((player1, player2), turns=rounds, noise=noise)
    result = match.play()
    for i in range(len(result)):
        result[i] = (result[i][0] == axl.Action.C, result[i][1] == axl.Action.C)
    return result
