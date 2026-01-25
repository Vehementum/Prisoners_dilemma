import bar_chart_race as bcr
import pandas as pd
from evolution.next_gen_axelrod import evolution_data_axelrod
from simulation.data_bcr import bcr_data
import pandas as pd
import numpy as np
from core.match_history import match_history_with_noise, score
import os
import importlib
from evolution.next_gen import create_strategies_pop, evolution_data, evolution_data_with_noise
import matplotlib.pyplot as plt


################################################## Creates the strategies dictionary from strategies folder ##############################

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

############################### Evolution Data and Plotting using strategies in strategies folder ##############################

# data = evolution_data(strategies, pop_size=100, generations=100, interval=5)
# data2 = evolution_data_with_noise(strategies, pop_size=100, generations=100, interval=5)

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


############################# Imports strategies from the axelrod library (first and second tournaments) ###################################################
from axelrod import (
    Random,
    TitForTat,
    SecondByAppold,
    SecondByBlack,
    SecondByBorufsen,
    SecondByCave,
    SecondByChampion,
    SecondByColbert,
    SecondByEatherley,
    SecondByGetzler,
    SecondByGladstein,
    SecondByGraaskampKatzen,
    SecondByGrofman,
    SecondByHarrington,
    SecondByKluepfel,
    SecondByLeyvraz,
    SecondByMikkelson,
    SecondByRichardHufford,
    SecondByRowsam,
    SecondByTester,
    SecondByTidemanAndChieruzzi,
    SecondByTranquilizer,
    SecondByWeiner,
    SecondByWhite,
    SecondByWmAdams,
    SecondByYamachi
)
axelrod_second_tournament_strategies = [
    # Baseline strategies used in the second tournament
    Random(),
    TitForTat(),
    
    # Specific submissions to the second tournament
    SecondByAppold(),
    SecondByBlack(),
    SecondByBorufsen(),
    SecondByCave(),
    SecondByChampion(),
    SecondByColbert(),
    SecondByEatherley(),
    SecondByGetzler(),
    SecondByGladstein(),
    SecondByGraaskampKatzen(),
    SecondByGrofman(),
    SecondByHarrington(),
    SecondByKluepfel(),
    SecondByLeyvraz(),
    SecondByMikkelson(),
    SecondByRichardHufford(),
    SecondByRowsam(),
    SecondByTester(),
    SecondByTidemanAndChieruzzi(),
    SecondByTranquilizer(),
    SecondByWeiner(),
    SecondByWhite(),
    SecondByWmAdams(),
    SecondByYamachi()
]
axelrod_second_fancy_names = [
    # Baseline strategies
    "Random",
    "Tit For Tat",
    
    # Specific submissions (Logic Mapping)
    "Appold"                    # A complex "Nice" strategy
    "Black",                    # A "Nice" variant
    "Borufsen",                 # A "Prober" / "Tester"
    "Cave",                     # A "Nice" strategy
    "Champion",                 # "The Statistical Prober"
    "Colbert",                  # A "Nasty" strategy
    "Eatherley",                # "The Doubler" (retaliates with increasing severity)
    "Getzler",                  # A "Nice" version of Tit For Tat
    "Gladstein",                # "The Tester"
    "Graaskamp & Katzen",       # "The Prober" (uses internal checks)
    "Grofman",                  # "The Random Cooperator" (2/7 probability)
    "Harrington",               # "The Genetic Explorer" (Uses long-range patterns)
    "Kluepfel",                 # A "Nice" strategy
    "Leyvraz",                  # A "Nasty" strategy
    "Mikkelson",                # A "Nice" strategy
    "Richard Hufford",          # A "Nice" strategy
    "Rowsam",                   # A "Nice" strategy
    "Tester",                   # "The Prober" (tests for Tit For Tat)
    "Tideman & Chieruzzi",      # "The Fresh Starter"
    "Tranquilizer",             # "The Sneaky Defector"
    "Weiner",                   # A "Nice" strategy
    "White",                    # A "Nice" strategy
    "Wm Adams",                 # A "Nice" strategy
    "Yamachi"                   # A "Nice" strategy
]
from axelrod import (
    Random,
    TitForTat,
    FirstByAnonymous,
    FirstByDavis,
    FirstByDowning,
    FirstByFeld,
    FirstByGraaskamp,
    FirstByGrofman,
    FirstByJoss,
    FirstByNydegger,
    FirstByShubik,
    FirstBySteinAndRapoport,
    FirstByTidemanAndChieruzzi,
    FirstByTullock
)

axelrod_first_strategies = [
    Random(),
    TitForTat(),
    FirstByAnonymous(),
    FirstByDavis(),
    FirstByDowning(),
    FirstByFeld(),
    FirstByGraaskamp(),
    FirstByGrofman(),
    FirstByJoss(),
    FirstByNydegger(),
    FirstByShubik(),
    FirstBySteinAndRapoport(),
    FirstByTidemanAndChieruzzi(),
    FirstByTullock()

]
axelrod_first_fancy_names = [
    "Random",
    "Tit For Tat",
    "Anonymous",
    "Grudger",
    "Revised Downing",
    "Feld",
    "Graaskamp",
    "Grofman",
    "Joss",
    "Nydegger",
    "Shubik",
    "Stein and Rapoport",
    "Tideman and Chieruzzi",
    "Tullock"
]

############################### Evolution Data and Plotting using strategies in axelrod library ##############################

strategy_dict_first_tournament = {}
for i in range(len(axelrod_first_fancy_names)):
    strategy_dict_first_tournament[axelrod_first_fancy_names[i]] = axelrod_first_strategies[i]

# data = evolution_data_axelrod(strategy_dict_first_tournament, pop_size=100, generations=50, interval=1)
# plot_evolution(data)

strategy_dict_second_tournament = {}
for i in range(len(axelrod_second_fancy_names)):
    strategy_dict_second_tournament[axelrod_second_fancy_names[i]] = axelrod_second_tournament_strategies[i]

data2 = evolution_data_axelrod(strategy_dict_second_tournament, pop_size=100, generations=50, interval=1)
plot_evolution(data2)