def s05(match_history):
    """Repeats last move if payoff was good; switches if it was bad."""
    if not match_history:
        return True
    if match_history[-1][0] == match_history[-1][1]:
        return match_history[-1][1]
    else:
        return not match_history[-1][1]