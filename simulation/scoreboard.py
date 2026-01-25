def scoreboard(scores):
    """Generates a sorted scoreboard from the scores dictionary."""
    results = []
    for keys in scores.keys():
        results.append((keys, scores[keys]))
    results.sort(key=lambda x: x[1], reverse=True)
    return results