import os
import importlib
strategies = {}

def get_num(strategy_name):
    return int(strategy_name[1:3])
for file in os.listdir("strategies"):
    if file.startswith("s") and file.endswith(".py") and file[1:3].isdigit() and get_num(file) <= 14:
        mod_name = "strategies." + file[:-3]
        module = importlib.import_module(mod_name)
        func_name = file[:3]
        function_object = getattr(module, func_name)
        strategies[func_name] = function_object

## Strategies in the following format :
## "s01" --> s01_always_coop.s01
## "s02" --> s02_always_defect.s02
## ...

from core.match_history import match_history, score
from simulation.round_robin import round_robin



print(match_history(strategies["s01"], strategies["s04"]))

print(score(match_history(strategies["s01"], strategies["s04"])))

print(round_robin(strategies, rounds=200))
