from axelrod_lib.test_axelrod import match_axl
from core.match_history import match_history, score, match_history_with_noise
import pandas as pd
import numpy as np
from evolution.next_gen import create_strategies_pop, score_coeff


def next_gen_axelrod(strategies_pop, interval=1):
    """Same as next_gen but the matches are with noise and it uses axelrod library strategies :
    Generates the next generation of strategies based on their scores and current population.
    Starts by resetting populations to 0 in the next_gen.
    Then, adds the scores from strategy X against all other X strategies (there are score(n) encounters where n is the population of strategy X) to next_gen.
    Then, adds the scores from strategy X against all other Y strategies (there are n*m encounters where n and m are the populations of strategies X and Y respectively) to next_gen.
    Then normalizes the populations based on total scores to create the next generation.
    Uses largest remainder method to ensure total population remains constant.
    next_gen: list of tuples (name, strategy_function, population)"""
    next_generation = strategies_pop.copy()
    for i in range(len(next_generation)):
        next_generation[i] = (next_generation[i][0], next_generation[i][1], 0)  # Reset population counts to 0
    total_pop = sum(i[2] for i in strategies_pop)
    total_score = 0
    for i in range(len(strategies_pop)):
        match_hist = match_axl(strategies_pop[i][1], strategies_pop[i][1], interval)
        score1, score2 = score(match_hist)
        total_score += score1*score_coeff(strategies_pop[i][2])
        next_generation[i] = (next_generation[i][0], next_generation[i][1], next_generation[i][2] + score1 * score_coeff(strategies_pop[i][2]))
    for i in range(len(strategies_pop)-1):
        for j in range(i+1, len(strategies_pop)):
            match_hist = match_axl(strategies_pop[i][1], strategies_pop[j][1], interval)
            score1, score2 = score(match_hist)
            total_score += (score1 + score2) * strategies_pop[i][2] * strategies_pop[j][2]
            next_generation[i] = (next_generation[i][0], next_generation[i][1], next_generation[i][2] + score1 * strategies_pop[i][2] * strategies_pop[j][2])
            next_generation[j] = (next_generation[j][0], next_generation[j][1], next_generation[j][2] + score2 * strategies_pop[i][2] * strategies_pop[j][2])
    # Normalize populations
    remainders = []
    for i in range(len(next_generation)): 
        if total_score > 0:
            next_generation[i] = (next_generation[i][0], next_generation[i][1], int((next_generation[i][2] / total_score) * total_pop))
            remainders.append(((next_generation[i][2] / total_score) * total_pop) - int((next_generation[i][2] / total_score) * total_pop))
        else:
            next_generation[i] = (next_generation[i][0], next_generation[i][1], total_pop // len(next_generation))
    for i in range(total_pop - sum(i[2] for i in next_generation)):
        max_index = remainders.index(max(remainders))
        next_generation[max_index] = (next_generation[max_index][0], next_generation[max_index][1], next_generation[max_index][2] + 1)
        remainders[max_index] = 0
    return next_generation

def evolution_data_axelrod(strategies, pop_size=100, generations=50, interval=5):
    """Simulates evolution of strategies over a number of generations.
    strategies: dict of strategy_name: strategy_function
    pop_size: total population size
    generations: number of generations to simulate
    interval: number of rounds per match"""
    strategies_pop = create_strategies_pop(strategies, pop_size)
    history = []
    for gen in range(generations):
        history.append([(s[0], s[2]) for s in strategies_pop])  # Store name and population
        strategies_pop = next_gen_axelrod(strategies_pop, interval)
    return history