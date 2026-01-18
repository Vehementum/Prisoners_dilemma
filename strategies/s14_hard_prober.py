def s14(match_history):
    """Plays C, D, D to probe, then defects if opponent always cooperated, else Tit-for-Tat."""
    if not match_history:
        return True
    if len(match_history) == 1:
        return False
    if len(match_history) == 2:
        return False
    if len(match_history) > 2:
        if match_history[0][1] and match_history[1][1] and match_history[2][1]:
            return False
        else:
            return match_history[-1][1]