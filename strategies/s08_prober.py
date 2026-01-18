def s08(match_history):
    """Plays C, D, C initially to probe, then defects if opponent always cooperated, else Tit-for-Tat."""
    if not match_history:
        return True
    if len(match_history) == 1:
        return False
    if len(match_history) == 2:
        return True
    if len(match_history) > 2 and match_history[0][1] and match_history[1][1] and match_history[2][1]:
        return False
    return match_history[-1][1]