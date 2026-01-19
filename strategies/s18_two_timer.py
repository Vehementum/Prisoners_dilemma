def s18(match_history):
    """Cooperates first, defects second, then defects if opponent defected last two moves, else alternates."""
    if not match_history:
        return True
    if len(match_history) == 1:
        return False
    else:
        if match_history[-2][1] == False and match_history[-1][1] == False:
            return match_history[-1][1]
    if len(match_history) % 2 == 1:
        return False
    return True

