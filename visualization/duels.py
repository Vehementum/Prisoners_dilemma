import bar_chart_race as bcr
import pandas as pd
from simulation.data_bcr import bcr_data, bcr_data_axelrod, bcr_data_axelrod2, final_scores_axelrod, print_scoreboard
import pandas as pd
import numpy as np
from core.match_history import match_history_with_noise, score
import os
import importlib


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
    FirstByTullock,
    Defector,
    TitFor2Tats
    
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


# data2 = bcr_data_axelrod(rounds=200, noise_prob=0, strategies=[TitForTat(), FirstByDavis()], strategies_names=["Tit For Tat", "Grudger"], interval=1)

# bcr.bar_chart_race(
#         df=data2,
#         filename='output/prisoners_dilemma_axelrod_duel_tit_for_tat_vs_grudger.gif', 
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


# data3 = bcr_data_axelrod(rounds=200, noise_prob=0, strategies=[TitForTat(), FirstByJoss()], strategies_names=["Tit For Tat", "Joss"], interval=1)
# print(data3)
# bcr.bar_chart_race(
#         df=data3,
#         filename='output/prisoners_dilemma_axelrod_duel_tit_for_tat_vs_joss.gif', 
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

# data4 = bcr_data_axelrod2(rounds=200, noise_prob=0, strategies=axelrod_first_strategies, strategies_names=axelrod_first_fancy_names, interval=1)
# bcr.bar_chart_race(
#         df=data4,
#         filename='output/prisoners_dilemma_axelrod_data4.gif', 
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

# tournament_15_1 = axelrod_first_strategies.copy()
# tournament_15_1.append(Defector())

# data5 = bcr_data_axelrod(rounds=200, noise_prob=0, strategies=tournament_15_1, strategies_names=axelrod_first_fancy_names + ["Defector"], interval=1)
# bcr.bar_chart_race(
#         df=data5,
#         filename='output/prisoners_dilemma_axelrod_tournament_15_1_defector.gif', 
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

# tournament_15_2 = axelrod_first_strategies.copy()
# tournament_15_2.append(TitFor2Tats())

# data5 = bcr_data_axelrod(rounds=200, noise_prob=0, strategies=tournament_15_2, strategies_names=axelrod_first_fancy_names + ["TitFor2Tats"], interval=1)
# bcr.bar_chart_race(
#         df=data5,
#         filename='output/prisoners_dilemma_axelrod_tournament_15_2_titfortwotats.gif', 
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
from axelrod import (
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
    SecondByYamachi,
    Adaptive,
    HardTitForTat,
    SoftJoss,
    Prober,
    Gradual,
    ContriteTitForTat,
    WinShiftLoseStay,
    BackStabber,
    SneakyTitForTat,
    ForgivingTitForTat,
    Aggravater,
    MetaHunter,
    MetaMajority,
    MetaMinority,
    AdaptiveTitForTat,
    Bully,
    Calculator,
    CautiousQLearner,
    EvolvedANN,
    Desperate,
    Detective,
    FoolMeOnce,
    HardProber,
    HardTitFor2Tats,
    Hopeless,
    Cycler,
    MetaWinner,
    NiceAverageCopier,
    Darwin,
    Michaelos,
    Thumper,
    ZDGTFT2,
    ZDExtort2,
    ZDSet2,
    Random,
    TitForTat,
    TitFor2Tats,
    Defector,
    Cooperator,
    Predator,
)

axelrod_second_tournament_strategies = [
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
    SecondByYamachi(),
    #Random(),
    TitForTat(),
    #TitFor2Tats(),
]


    # Baseline strategies used in the second tournament

axelrod_second_fancy_names = [
    "Appold",
    "Black",
    "Borufsen",
    "Cave",
    "Champion",
    "Colbert",
    "Eatherley",
    "Getzler",
    "Gladstein",
    "Graaskamp-Katzen",
    "Grofman",
    "Harrington",
    "Kluepfel",
    "Leyvraz",
    "Mikkelson",
    "Richard Hufford",
    "Rowsam",
    "Tester",
    "Tideman and Chieruzzi",
    "Tranquilizer",
    "Weiner",
    "White",
    "Wm Adams",
    "Yamachi",
    "Random",
    "TitForTat",
    "TitFor2Tats",

]

data6 = bcr_data_axelrod(rounds=200, noise_prob=0, strategies=axelrod_second_tournament_strategies, strategies_names=axelrod_second_fancy_names, interval=1)
results = final_scores_axelrod(data6)
print_scoreboard(results)
bcr.bar_chart_race(
        df=data6,
        filename='output/prisoners_dilemma_axelrod_tournament_64.gif', 
        orientation='h', 
        sort='desc', 
        n_bars=8, 
        fixed_order=False, 
        fixed_max=True,
        steps_per_period=20, 
        period_length=500, 
        interpolate_period=False, 
        period_label={'x': .98, 'y': .3, 'ha': 'right', 'va': 'center'}, 
        period_summary_func=lambda v, r: {'x': .98, 'y': .2, 
                                          's': f'Total score: {v.sum():,.0f}', 
                                          'ha': 'right', 'size': 11}, 
        title='Prisoners Dilemma Strategies Scoreboard Over Time', 
        bar_size=.95, 
        shared_fontdict=None, 
        scale='linear', 
        fig=None, 
        writer=None, 
        )

# data7 = bcr_data_axelrod(rounds=200, noise_prob=0.1, strategies=axelrod_second_tournament_strategies, strategies_names=axelrod_second_fancy_names, interval=1)
# bcr.bar_chart_race(
#         df=data7,
#         filename='output/prisoners_dilemma_axelrod_tournament_64_noise.gif', 
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