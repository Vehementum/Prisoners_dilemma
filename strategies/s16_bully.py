def s16(match_history):
    """Defects first, then if opponent defects back, cooperates, then defect again."""
    if not match_history:
        return False
    if len(match_history) == 1:
        return match_history[-1][1]
    else:
        if match_history[-2][0] == False and match_history[-1][1] == False:
            return True
        else:
            return False

