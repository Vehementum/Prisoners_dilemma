import bar_chart_race as bcr
import pandas as pd
from simulation.data_bcr import bcr_data
import pandas as pd
import numpy as np
from core.match_history import match_history_with_noise, score
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

data = bcr_data(rounds=2000, noise_prob=0.1, strategies=strategies, interval=5)
bcr.bar_chart_race(
        df=data,
        filename='output/prisoners_dilemma_horiz.gif', 
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