def s07(match_history):
    """Defects first, then copies the opponent's previous move."""
    if not match_history:
        return False
    return match_history[-1][1]