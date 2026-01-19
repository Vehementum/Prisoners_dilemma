import random

def noise(move, probability=0.1):
    """Flips the move with a probability p to simulate noise."""
    if random.random() < probability:
        return not move
    return move