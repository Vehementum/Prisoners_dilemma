def s17(match_history):
    """Defects first, then defects if opponent cooperated at least half the time, else mimics opponent's last move."""
    if not match_history:
        return False
    rate_coop = sum(1 for m in match_history if m[1] == True) / len(match_history)
    if rate_coop >= 0.5:
        return False
    else:
        return match_history[-1][1]

