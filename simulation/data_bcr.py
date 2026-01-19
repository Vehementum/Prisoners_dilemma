import pandas as pd
import numpy as np
from core.match_history import match_history_with_noise, score

def bcr_data(rounds, noise_prob, strategies, interval=10):
    data = {name: [] for name in strategies.keys()}
    for r in range(0, rounds + 1, interval):
        scores = {name: 0 for name in strategies.keys()}
        for i in range(len(strategies)):
            for j in range(i + 1, len(strategies)):
                name1 = list(strategies.keys())[i]
                name2 = list(strategies.keys())[j]
                strat1 = strategies[name1]
                strat2 = strategies[name2]
                match_hist = match_history_with_noise(strat1, strat2, r, noise_prob)
                score1, score2 = score(match_hist)
                scores[name1] += score1
                scores[name2] += score2
        for name in strategies.keys():
            data[name].append(scores[name])
    df = pd.DataFrame(data)
    df.index = np.arange(0, rounds + 1, interval)
    return df

