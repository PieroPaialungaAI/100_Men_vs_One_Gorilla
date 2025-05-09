from gorilla import Gorilla
from human import Human


def run_single_round_simulation(print_statement = False):
    gorilla = Gorilla()
    human = Human()
    start_resistance, gorilla_strength = human.resistance.copy(), gorilla.strength.copy()
    gorilla.take_damage(human_strength = human.strength)
    is_human_alive = human.alive
    round_count = 0
    while is_human_alive:
        if print_statement:
            print(f'Human vs Gorilla, round {round_count}')
            print(f'Human has resistance =  {human.resistance}, he gets hit by strength = {gorilla.strength}')
        human.take_damage(gorilla_strength=gorilla.strength)
        if print_statement:
            print(f'Human has now resistance {human.resistance}')
        is_human_alive = human.alive
        round_count += 1
    if print_statement:
        print(f'Human is dead after {round_count} rounds')
    return round_count, start_resistance, gorilla_strength


def run_multiple_round_simulations(num_simulations = 10**5, print_statement = False):
    round_count_list = []
    resistance_list = []
    strength_list = []
    for _ in range(num_simulations):
        simulation, human_resistance, gorilla_strength = run_single_round_simulation(print_statement)
        round_count_list.append(simulation)
        resistance_list.append(human_resistance)
        strength_list.append(gorilla_strength)
    return round_count_list, resistance_list, strength_list


def run_full_simulation(gorilla, population):
    pass