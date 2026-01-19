import random
def s15(match_history):
    """Cooperates first, then copies the opponent's previous move with random chance of defection."""
    if not match_history:
        return True
    else:
        if random.random() < 0.1:  # 10% chance to defect
            return False
        return match_history[-1][1]
