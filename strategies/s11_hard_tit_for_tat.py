def s11(match_history):
    """Cooperates first, then copies opponent's last move without forgiveness."""
    if not match_history:
        return True
    return match_history[-1][1]