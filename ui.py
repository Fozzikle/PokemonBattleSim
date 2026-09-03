from pokemon import Move, Pokemon, add_move, add_pokemon
from battle import battle, loading
import random
import time


# UI for user to select their Pokémon and who they verse.
# UI should show user the health of both Pokémon, allow the player to choose their attack, show result of their attack
# TODO: Maybe in future, CSV pokemon and moves/attacks and call from there

# TODO: Somehow group in the print statement "Your Opponent is now choosing their pokemon" with the loading such it is
#       inclusive when rewritten later on


# Creating basic terminal version
if __name__ == "__main__":
    # Adding to environment some default moves/attacks
    thunderbolt: Move = Move(
        name="Thunderbolt",
        power=90,
        accuracy=70
    )

    tackle: Move = Move(
        name="Tackle",
        power=40,
        accuracy=100
    )

    pound: Move = Move(
        name="Pound",
        power=40,
        accuracy=100
    )

    karate_chop: Move = Move(
        name="Karate Chop",
        power=50,
        accuracy=100
    )

    cut: Move = Move(
        name="Cut",
        power=50,
        accuracy=95
    )

    scratch: Move = Move(
        name="Scratch",
        power=40,
        accuracy=100
    )

    take_down: Move = Move(
        name="Take Down",
        power=90,
        accuracy=85
    )

    zap_cannon: Move = Move(
        name="Zap Cannon",
        power=120,
        accuracy=50
    )

    mirror_shot: Move = Move(
        name="Mirror Shot",
        power=65,
        accuracy=85
    )

    # adding to environment some default pokemon
    pikachu: Pokemon = Pokemon(
        "Pikachu",
        health=100,
        defence=40,
        speed=90,
        moves=[thunderbolt, tackle]
    )

    chespin: Pokemon = Pokemon(
        "Chespin",
        health=56,
        defence=65,
        speed=38,
        moves=[scratch, zap_cannon, cut]
    )

    bidoof: Pokemon = Pokemon(
        "Bidoof",
        health=59,
        defence=40,
        speed=31,
        moves=[karate_chop, pound, thunderbolt]
    )

    # Collection of Pokémon
    pokemon = [pikachu.name, chespin.name, bidoof.name]
    pokemon_obj = [pikachu, chespin, bidoof]
    formatted_pokemon = ", ".join(pokemon)

    # Collection of moves
    moves = [
        thunderbolt.name,
        tackle.name,
        pound.name,
        karate_chop.name,
        cut.name,
        scratch.name,
        take_down.name,
        zap_cannon.name,
        mirror_shot.name
    ]
    moves_obj = [
        thunderbolt,
        tackle,
        pound,
        karate_chop,
        cut,
        scratch,
        take_down,
        zap_cannon,
        mirror_shot
    ]
    formatted_moves = ", ".join(moves)
    # Prompt player to choose a Pokémon
    # TODO: Add a confirmation stage for player to confirm their selection
    # TODO: Rework order of operations of user interactions in UI
    # TODO: add parameters that prevent users from adding a completely overpowered pokemon or move (partially done).
    #       -check for balance too for the added moves.

    # TODO: When running while true loop, apply the rewrite function of input such it clears after that section has
    #       been completed like the rest of the code

    # User loop for creating new Pokémon and adding moves
    # TODO: in future add helper function of variations of valid inputs + add confirmations of success for each action
    while True:
        print("For the following questions if you would like to perform said action please type 'yes'")
        if input("Did you want to add a move? ") == "yes":
            add_move(moves, moves_obj)

        if input("Did you want to make a Pokemon? ") == "yes":
            add_pokemon(pokemon, pokemon_obj, formatted_moves, moves_obj, moves)

        else:
            break

    # User Pokémon selection loop
    while True:
        player_pokemon_str = input(f"Available Pokemon: {formatted_pokemon}\nChoose your Pokémon: ")

        if player_pokemon_str in pokemon:
            print("\rPokémon Selected!", end="")
            time.sleep(0.5)
            break

    # get AI to choose a Pokémon
    # randomly select an index for list Pokémon
    ai_pokemon_index = random.randint(0, len(pokemon) - 1)

    # fake thinking time of AI choosing its Pokémon
    loading(10)

    # Applying index to list to select their Pokémon
    ai_pokemon = pokemon_obj[ai_pokemon_index]
    ai_pokemon_str = str(pokemon[ai_pokemon_index])
    print("\rYour opponent has selected: " + ai_pokemon_str)

    # converting user selection to object
    # todo: make this a function and update pokemon.py and battle.py
    index = pokemon.index(player_pokemon_str)
    player_pokemon: Pokemon = pokemon_obj[index]

    # battle sequence
    winner = battle(player_pokemon, ai_pokemon)
    print(f"{winner[0]} won the battle using {winner[1].title()}")
