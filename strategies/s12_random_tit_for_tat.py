from random import random
p = 0.7

def s12(match_history):
    """Copies opponent's last move with probability p, defects randomly otherwise."""
    if not match_history:
        return True
    if random() < p:
        return match_history[-1][1]
    else:
        return False