import pandas as pd
import numpy as np
from core.match_history import match_history_with_noise, score
from axelrod_lib.test_axelrod import match_axl
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

payoff = {
    (True, True): (3, 3),
    (True, False): (0, 5),
    (False, True): (5, 0),
    (False, False): (1, 1)
}

def bcr_data_axelrod(rounds, noise_prob, strategies, strategies_names, interval=10):
    import axelrod as axl
    data = {name: [0 for i in range(0, rounds + 1, interval)] for name in strategies_names}
    for i in range(len(strategies)):
        for j in range(i + 1, len(strategies)):
            name1 = strategies_names[i]
            name2 = strategies_names[j]
            strat1 = strategies[i]
            strat2 = strategies[j]
            match_hist = match_axl(strat1, strat2, rounds, noise_prob)
            scores = {name1: 0, name2: 0}
            for r in range(0, rounds):
                score1, score2 = payoff[match_hist[r]]
                scores[name1] += score1
                scores[name2] += score2
                if (r + 1) % interval == 0:
                    data[name1][(r+1)//interval] = scores[name1] + data[name1][(r+1)//interval]
                    data[name2][(r+1)//interval] = scores[name2] + data[name2][(r+1)//interval]
    df = pd.DataFrame(data)
    return df


def bcr_data_axelrod2(rounds, noise_prob, strategies, strategies_names, interval=10):
    import axelrod as axl
    data = {name: [0 for i in range(0, rounds + 1, interval)] for name in strategies_names}
    for i in range(len(strategies)):
        for j in range(i + 1, len(strategies)):
            name1 = strategies_names[i]
            name2 = strategies_names[j]
            strat1 = strategies[i]
            strat2 = strategies[j]
            match_hist = match_axl(strat1, strat2, rounds, noise_prob)
            scores = {name1: 0, name2: 0}
            for r in range(0, rounds):
                score1, score2 = payoff[match_hist[r]]
                scores[name1] += score1
                scores[name2] += score2
                if (r + 1) % interval == 0:
                    data[name1][(r+1)//interval] = scores[name1] + data[name1][(r+1)//interval]
                    data[name2][(r+1)//interval] = scores[name2] + data[name2][(r+1)//interval]
    for i in range(len(strategies)):
        match_hist = match_axl(strategies[i], strategies[i], rounds, noise_prob)
        score = 0
        for r in range(0, rounds):
            score1, score2 = payoff[match_hist[r]]
            score += score1
            if (r + 1) % interval == 0:
                data[strategies_names[i]][(r+1)//interval] = score + data[strategies_names[i]][(r+1)//interval]
    df = pd.DataFrame(data)
    print(df)
    return df

def final_scores_axelrod(data):
    scores = {}
    for col in data.columns:
        scores[col] = data[col].iloc[-1]
    return scores


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


# data = bcr_data_axelrod(rounds=200, noise_prob=0, strategies=axelrod_first_strategies, strategies_names=axelrod_first_fancy_names, interval=2)
# print(data)
# scores = final_scores_axelrod(data)
# print(scores)