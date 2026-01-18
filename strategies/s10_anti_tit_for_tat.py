def s10(match_history):
    """Does the opposite of the opponent's last move; first move cooperates."""
    if not match_history:
        return True
    return not match_history[-1][1]