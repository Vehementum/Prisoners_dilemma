def scoreboard(scores):
    results = []
    for keys in scores.keys():
        results.append((keys, scores[keys]))
    results.sort(key=lambda x: x[1], reverse=True)
    return results