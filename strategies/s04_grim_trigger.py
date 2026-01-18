def s04(match_history):
    """Cooperates until the opponent defects once, then defects forever."""
    if not match_history:
        return True
    if False in [move[1] for move in match_history]:
        return False
    return True