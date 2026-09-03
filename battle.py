from pokemon import Pokemon, Move
import numpy as np
import time


def loading(think_time: int) -> None:
    """
    Loading bar for the fake thinking time of AI.
    Does a "Loading..." animation indicating loading
    """
    # Calculating number of times the complete animation will happen
    full_loop: int = think_time % 4

    # creating the loading loop
    loop_index: int = 0
    load_dot_index: int = 0
    while loop_index <= full_loop:
        dots = "." * load_dot_index
        time.sleep(0.5)
        print("\rThinking" + dots, end="")
        if load_dot_index < 3:
            load_dot_index += 1
        else:
            load_dot_index = 0
            loop_index += 1
    return


def calc_start_order(user_pokemon: Pokemon, ai_pokemon: Pokemon) -> bool:
    speed_dif = user_pokemon.speed - ai_pokemon.speed
    return speed_dif > 0


def fight_sequence(pokemon_order_1: Pokemon, pokemon_order_2: Pokemon, turn_owner: str) -> None:
    available_moves = pokemon_order_1.moves
    str_available_moves = []
    for i in range(len(available_moves)):
        x = available_moves[i].name.lower()
        str_available_moves.append(x)

    # Switch for if user or AI is attacking
    match turn_owner:
        case "user":
            while True:
                print(f"Available moves: {str_available_moves}")  # TODO: improve format of print
                input_move = input("What attack will you use? ")

                try:
                    index = str_available_moves.index(input_move)
                    selected_move: Move = available_moves[index]
                    attack_results = pokemon_order_2.take_damage(selected_move)
                    print(f"{pokemon_order_1.name} used {input_move.title()} and dealt {attack_results[1]} damage")
                    print(f"{pokemon_order_2.name} now has {attack_results[0]} health")
                    break

                except ValueError:
                    print("This is not a valid move")

            return

        case "ai":
            print("\rOOF", end='')
            time.sleep(1)
            loading(10)
            rng = np.random.default_rng()
            index = rng.integers(low=0, high=len(available_moves))
            selected_move: Move = available_moves[index]
            attack_results = pokemon_order_2.take_damage(selected_move)
            print(f"{pokemon_order_1.name} used {selected_move.name} and dealt {attack_results[1]} damage")
            print(f"{pokemon_order_2.name} now has {attack_results[0]} health")


def battle(user_pokemon: Pokemon, ai_pokemon: Pokemon) -> tuple[str, str]:
    move_order = calc_start_order(user_pokemon, ai_pokemon)
    while True:
        if ai_pokemon.health and user_pokemon.health > 0:
            match move_order:
                case True:
                    fight_sequence(user_pokemon, ai_pokemon, turn_owner="user")
                    move_order = False

                case False:
                    fight_sequence(ai_pokemon, user_pokemon, turn_owner="ai")
                    move_order = True

        elif ai_pokemon.health == 0:
            return "User", user_pokemon.name

        else:
            return "AI", ai_pokemon.name
