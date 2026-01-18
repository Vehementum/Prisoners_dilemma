def s09(match_history):
    """Cooperates unless the opponent defected in both of the last two moves."""
    if not match_history:
        return True
    if len(match_history) == 1:
        return True
    if len(match_history) > 1:
        if not match_history[-1][1] and not match_history[-2][1]:
            return False
        else:
            return True