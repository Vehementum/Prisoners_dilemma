def s03(match_history):
    """Cooperates first, then copies the opponent's previous move."""
    if not match_history:
        return True
    else:
        return match_history[-1][1]