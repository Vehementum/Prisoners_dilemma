import bar_chart_race as bcr
import pandas as pd
from simulation.data_bcr import bcr_data, bcr_data_axelrod
import pandas as pd
import numpy as np
from core.match_history import match_history_with_noise, score
import os
import importlib

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

############################################### Prisoners Dilemma Racing Bar Chart Data and Plotting using strategies in strategies folder ##############################

# data = bcr_data(rounds=200, noise_prob=0, strategies=strategies, interval=2)
# bcr.bar_chart_race(
#         df=data,
#         filename='output/prisoners_dilemma_horiz.gif', 
#         orientation='h', 
#         sort='desc', 
#         n_bars=8, 
#         fixed_order=False, 
#         fixed_max=True,
#         steps_per_period=20, 
#         period_length=500, 
#         interpolate_period=False, 
#         period_label={'x': .98, 'y': .3, 'ha': 'right', 'va': 'center'}, 
#         period_summary_func=lambda v, r: {'x': .98, 'y': .2, 
#                                           's': f'Total score: {v.sum():,.0f}', 
#                                           'ha': 'right', 'size': 11}, 
#         title='Prisoners Dilemma Strategies Scoreboard Over Time', 
#         bar_size=.95, 
#         shared_fontdict=None, 
#         scale='linear', 
#         fig=None, 
#         writer=None, 
#         ) 


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

############################## Prisoners Dilemma Racing Bar Chart Data and Plotting using strategies in axelrod library ######################################

# data2 = bcr_data_axelrod(rounds=200, noise_prob=0, strategies=axelrod_first_strategies, strategies_names=axelrod_first_fancy_names, interval=4)
# print(data2)
# bcr.bar_chart_race(
#         df=data2,
#         filename='output/prisoners_dilemma_axelrod.gif', 
#         orientation='h', 
#         sort='desc', 
#         n_bars=8, 
#         fixed_order=False, 
#         fixed_max=True,
#         steps_per_period=20, 
#         period_length=1500, 
#         interpolate_period=False, 
#         period_label={'x': .98, 'y': .3, 'ha': 'right', 'va': 'center'},
#         period_summary_func=lambda v, r: {'x': .98, 'y': .2, 
#                                           's': f'Total score: {v.sum():,.0f}',
#                                           'ha': 'right', 'size': 11},
#         title='Prisoners Dilemma Strategies Scoreboard Over Time',
#         bar_size=.95, 
#         shared_fontdict=None, 
#         scale='linear', 
#         fig=None, 
#         writer=None, 
#         ) 