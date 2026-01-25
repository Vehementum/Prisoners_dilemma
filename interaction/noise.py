import random

def noise(move, probability=0.1):
    """Flips the move with a probability p to simulate noise.
    Noise is simulated as misinterpreting the intended move."""
    if random.random() < probability:
        return not move
    return move