def s13(match_history):
    """Cooperates until the opponent defects twice, then defects forever."""
    if not match_history:
        return True
    if len(match_history) == 1:
        return True
    num_def = 0
    for move in match_history:
        if not move[1]:
            num_def +=1
            if num_def >= 2:
                return False
    return True