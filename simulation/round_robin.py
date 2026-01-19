from core.match_history import match_history, score

def round_robin(strategies, rounds):
    results = {}
    for keys in strategies.keys():
        results[keys] = 0
    strategy_names = list(strategies.keys())
    for i in range(len(strategy_names)-1):
        for j in range(i+1, len(strategy_names)):
            name1 = strategy_names[i]
            name2 = strategy_names[j]
            strat1 = strategies[name1]
            strat2 = strategies[name2]
            match_hist = match_history(strat1, strat2, rounds)
            score1, score2 = score(match_hist)
            results[name1] += score1
            results[name2] += score2
    return results

from core.match_history import match_history_with_noise

def round_robin_with_noise(strategies, rounds, noise_prob):
    results = {}
    for keys in strategies.keys():
        results[keys] = 0
    strategy_names = list(strategies.keys())
    for i in range(len(strategy_names)-1):
        for j in range(i+1, len(strategy_names)):
            name1 = strategy_names[i]
            name2 = strategy_names[j]
            strat1 = strategies[name1]
            strat2 = strategies[name2]
            match_hist = match_history_with_noise(strat1, strat2, rounds, noise_prob)
            score1, score2 = score(match_hist)
            results[name1] += score1
            results[name2] += score2
    return results