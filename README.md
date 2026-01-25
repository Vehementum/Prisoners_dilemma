# Prisoner’s Dilemma — A attempt at reproducing the findings in the official axelrod tournament and having a bit of fun along the way

## Overview

This project implements and explores **Iterated Prisoner’s Dilemma tournaments** inspired by Robert Axelrod’s work, with a focus on:

- Implementing strategies
- Visualizing the tournament results in the form of a racing bar chart
- Implementing noise
- Implementing evolution over time
- Visualizing evolution over time in the form of a graph

The goal is **not** to reuse an existing framework, but to **rebuild the core mechanisms from scratch** in a controlled, extensible way, enabling clear experimentation and interpretation. In the end, we imported the official strategies used in the axelrod tournament as we don't have the time nor ressources to implement the various complex
strategies created by various researchers in the official tournaments.

---

## Core Ideas

- Strategies are implemented as **pure functions**:
  - Input: match history
  - Output: `True` (cooperate) or `False` (defect)
- Tournaments are run in a **round-robin** fashion
- Payoffs follow the classical Prisoner’s Dilemma matrix
- Noise is introduced as **misinterpretation of opponent actions**
- Results are analyzed and visualized independently from simulation logic

---

## Project Structure
```
Prisoners_dilemma/
|
├── axelrod_lib/        # enabling use of axelrod strategies in our code
│
├── core/               # Core mechanics (match history, scoring)
│
├── strategies/         # Individual strategy implementations
│   ├── s01_*.py
│   ├── s02_*.py
│   └── ...
|
├── outputs/            # Outputs of the racing bar charts
│
├── simulation/         # Round robin tournaments, aggregations
│
├── interaction/        # (Planned) interaction filtering / persistence
│
├── evolution/          # Population dynamics over time
│
├── metrics/            # Score aggregation, rankings
│
└── visualization/      # Plots, racing bar charts

````

Each layer has a **single responsibility**:
- `simulation` produces data
- `visualization` consumes data
- strategies are isolated and interchangeable

---

## Strategies

The project includes a growing set of strategies inspired by Axelrod’s tournament, including:

### Cooperative / Reciprocal
- Always Cooperate
- Tit for Tat
- Generous Tit for Tat
- Suspicious Tit for Tat

### Retaliatory
- Grim Trigger
- Hard / Soft Grudger
- Delayed Grim

### Adaptive
- Win–Stay Lose–Shift (Pavlov)
- Conditional strategies based on opponent behavior

### Exploitative
- Opportunists
- Probers
- Bullies
- Noise-exploiting strategies

The emphasis is on **behavioral archetypes**, not exhaustive reproduction of all 63 historical strategies.

---

## Noise Model

Noise is implemented as a **probability of misperception**:
- A strategy may observe the opponent’s action incorrectly
- This directly impacts:
  - Retaliation
  - Forgiveness
  - Long-term cooperation stability

Noise can be tuned globally to explore robustness and collapse.

---

## Simulation Output

Simulations produce:
- Full match histories
- Cumulative scores per strategy over time
- Rankings at each round

These outputs are intentionally kept **library-agnostic** to allow flexible analysis and visualization.

---

## Visualization

The project uses:
- Static plots (scores, rankings)
- **Racing bar charts** to visualize dominance shifts over time

Visualization code is fully decoupled from simulation logic.

---

## Design Philosophy

- **Clarity over cleverness**
- **Explicit mechanisms over black boxes**
- **Reproducibility over performance**
- **Interpretability over optimization**

This is a modeling and reasoning project first, not a benchmarking exercise.

---

## Planned Extensions

- Interaction filtering (agents stop playing consistently exploitative opponents)
- Population evolution (selection pressure over time)
- Comparative analysis against Axelrod’s original results

---

## Requirements

- Python 3.10+
- pandas
- matplotlib
- bar_chart_race
- axelrod

---

## Implementations

After installing all the necessary libraries, to run the code, run the command ```python -m folder_name/python_file```
like so ```python -m visualization.data_rbc```

## Motivation

This project exists to answer one question:

> *Under realistic conditions (noise, exploitation, limited interaction), which forms of cooperation actually survive?*
