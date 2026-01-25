import os
import importlib
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

## Strategies in the following format :
## "s01" --> s01_always_coop.s01
## "s02" --> s02_always_defect.s02
## ...

from core.match_history import match_history, score, match_history_with_noise
from simulation.round_robin import round_robin, round_robin_with_noise
from simulation.scoreboard import scoreboard
from simulation.data_bcr import bcr_data
from evolution.next_gen import evolution_data, next_gen, create_strategies_pop

duel = match_history(strategies["s03"], strategies["s15"])
print(duel)
print(score(duel))
# print (score(match_history_with_noise(strategies["s03"], strategies["s04"], noise_prob=0.1)))
# print(match_history(strategies["s03"], strategies["s04"]))
# print(match_history_with_noise(strategies["s03"], strategies["s04"], noise_prob=0.1))

# data = round_robin(strategies, rounds=200)
# data_noise = round_robin_with_noise(strategies, rounds=200, noise_prob=0.1)
# # print(data)
# print (scoreboard(data))
# # print(data_noise)
# print (scoreboard(data_noise))

# print(bcr_data(rounds=200, noise_prob=0, strategies=strategies, interval=2))
# print(create_strategies_pop(strategies, pop_size=100))
# print(evolution_data(strategies, pop_size=100, generations=10, interval=5))