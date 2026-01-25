import bar_chart_race as bcr
import pandas as pd
import axelrod
from simulation.data_bcr import bcr_data
import pandas as pd
import numpy as np
from core.match_history import match_history_with_noise, score
import os
import importlib
from evolution.next_gen import create_strategies_pop, evolution_data, evolution_data_with_noise
import matplotlib.pyplot as plt
from axelrod_lib.test_axelrod import match_axl
from visualization.graph_evol import plot_evolution

payoff_matrix = {
    (True, True): (3, 3),      # Both cooperate
    (True, False): (0, 5),     # Player 1 cooperates, Player 2 defects
    (False, True): (5, 0),     # Player 1 defects, Player 2 cooperates
    (False, False): (1, 1)     # Both defect
}

def match_to_data_graph(match, strategy1_name, strategy2_name):
    data = []
    for move1, move2 in match:
        data.append([(strategy1_name, payoff_matrix[(move1, move2)][0]), (strategy2_name, payoff_matrix[(move1, move2)][1])])
    return data

def match_to_data_rbc(match, strategy1_name, strategy2_name):
    coop_counts = {strategy1_name: 0, strategy2_name: 0}
    data = []
    for move1, move2 in match:
        if move1:
            coop_counts[strategy1_name] += 1
        if move2:
            coop_counts[strategy2_name] += 1
        data.append(coop_counts.copy())
    df = pd.DataFrame(data)
    return df

print(match_axl(axelrod.TitForTat(), axelrod.Grudger(), 10))
data = match_to_data_graph(match_axl(axelrod.TitForTat(), axelrod.Grudger(), 10), "TitForTat", "Grudger")
print(data)
# data2 = match_to_data_rbc(match_axl(axelrod.TitForTat(), axelrod.Grudger(), 200), "TitForTat", "Grudger")
# print(data2)


# plot_evolution(data)