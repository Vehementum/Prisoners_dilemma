import bar_chart_race as bcr
import pandas as pd
from simulation.data_bcr import bcr_data
import pandas as pd
import numpy as np
from core.match_history import match_history_with_noise, score
import os
import importlib
from evolution.next_gen import create_strategies_pop, evolution_data, evolution_data_with_noise
import matplotlib.pyplot as plt
strategies = {}

def get_num(strategy_name):
    return int(strategy_name[1:3])
for file in os.listdir("strategies"):
    if file.startswith("s") and file.endswith(".py") and file[1:3].isdigit() and get_num(file) <= 18:
        mod_name = "strategies." + file[:-3]
        module = importlib.import_module(mod_name)
        func_name = file[:3]
        function_object = getattr(module, func_name)
        strategies[func_name] = function_object

data = evolution_data(strategies, pop_size=100, generations=100, interval=5)
print(data)
data2 = evolution_data_with_noise(strategies, pop_size=100, generations=100, interval=5)
def plot_evolution(data):
    generations = len(data)
    strategy_names = [name for name, _ in data[0]]
    populations = {name: [] for name in strategy_names}
    for gen_data in data:
        for name, pop in gen_data:
            populations[name].append(pop)
    for name, pops in populations.items():
        plt.plot(range(generations), pops, label=name)
    plt.xlabel('Generation')
    plt.ylabel('Population')
    plt.title('Evolution of Strategies Over Generations')
    plt.legend()
    return plt.show()

# plot_evolution(data)
# plot_evolution(data2)