def swap_history(match_history):
    result = []
    for move in match_history:
        result.append((move[1], move[0]))
    return result

def match_history(strategy1, strategy2, rounds=200):
    match_history = []
    for i in range(rounds):
        match_history.append((strategy1(match_history), strategy2(swap_history(match_history))))
    return match_history

payoff = {
    (True, True): (3, 3),
    (True, False): (0, 5),
    (False, True): (5, 0),
    (False, False): (1, 1)
}
def score(match_history):
    r1 = 0
    r2 = 0
    for move1, move2 in match_history:
        r1_add, r2_add = payoff[(move1, move2)]
        r1 += r1_add
        r2 += r2_add
    return (r1, r2)

def match_history_with_noise(strategy1, strategy2, rounds=200, noise_prob=0.01):
    from interaction.noise import noise
    match_history = []
    for i in range(rounds):
        move1 = strategy1(match_history)
        move2 = strategy2(swap_history(match_history))
        move1_noisy = noise(move1, noise_prob)
        move2_noisy = noise(move2, noise_prob)
        match_history.append((move1_noisy, move2_noisy))
    return match_history