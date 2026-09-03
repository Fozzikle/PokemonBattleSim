import time
import numpy as np


# GENERAL TODO: Go through and update comments
class Move:
    def __init__(self, name, power, accuracy):
        self.name = name
        self.power = power
        self.accuracy = accuracy


# Create Pokémon object with parameters name, HP, attack, defence, speed, list of move objects
# in future todo: add Pokémon types (water, fire, etc) achieved through inheritance (maybe)
class Pokemon:
    def __init__(self, name: str, health: int, defence: int, speed: int, moves: list):
        self.name = name
        self.health = health
        self.defence = defence
        self.speed = speed
        self.moves = moves

    def take_damage(self, move: Move) -> tuple[int, int]:
        """
        Calculates the damage a Pokémon will take from an attack. Uses the formula
        damage_from_attack = attack * ( X / (X + Defence))
        where X is a scaler

        This makes defence multiplicative such that if X = 100 and defence = 100, the damage taken from the attack is
        halved this will need balancing and adjustments based on how defence is implemented i.e. is it in the hundreds
        or tens of.
        """

        # Tweaking of the 50 value maybe needed
        effective_damage: int = round(pokemon_attack(move) * (50 / (50 + self.defence)))
        self.health -= effective_damage
        return self.health, effective_damage


# future TODO: add another scaler type which affects damage output based on effectiveness of that type vs another
#                 e.g. fire type vs water
# future TODO: implement speed as a factor of attack (low speed increase chance of opponent to dodge
def pokemon_attack(move: Move) -> int:
    """
    input determines which move is performed
    based on the move, calc if move will hit or miss based on accuracy + accuracy/effectiveness of attack
    if move miss, damage = 0
    if move hit calc damage output based on how accurate it was (% of damage based on accuracy int)
    move accuracy calc generate a random number based on a normal distribution skewed and centered by the
    accuracy stated in the move object

    Note: in the normal distribution, the sd of 0.1667 makes it so that the range 0-1 exists within 3 sd from the centre
    """

    # Sample normal distribution with skewed centre
    centre: float = move.accuracy / 100
    sample_normal_distribution: float = np.random.normal(centre, 0.1667)

    # bounding the sample to a percentage
    attack_accuracy: np.float64 = np.clip(sample_normal_distribution, 0, 1)
    # calc damage as move power scaled by attack_accuracy
    damage: int = round(move.power * attack_accuracy)

    # return attack damage int used for the take_damage method of other Pokémon
    return damage


def validate_int_input(prompt: str, minimum: int, maximum: int) -> int:
    fail_print = f"Input needs to be an integer between {minimum} and {maximum}"
    while True:
        try:
            user_input = int(input(prompt))

            if minimum < user_input < maximum:
                return user_input

            else:
                print(fail_print)

        except ValueError:
            print(fail_print)


# TODO: Rework balance checks for power and accuracy
def add_move(moves: list, moves_obj: list) -> None:
    while True:
        name: str = input("What is the name of this move? ")
        if name not in set(moves):
            break
        else:
            print("This move already exists!")
            time.sleep(1)

    while True:
        power = validate_int_input("How strong is this move?", 1, 100)
        accuracy = validate_int_input("How accurate is this move?", 1, 100)

        if power or accuracy < 70:
            break

        else:
            print("\rPower and Accuracy are not balanced!")
            time.sleep(1)
            print("\rPower and Accuracy cannot be both above 70!")

    new_move = Move(
        name=name,
        power=power,
        accuracy=accuracy
    )
    # updating available move list with new move
    moves.append(new_move.name)
    moves_obj.append(new_move)
    return


def allocate_moves_pokemon(formatted_moves: str, moves_obj: list, moves_available: list) -> list:
    # storing moves of the new Pokémon
    moves = []

    # storing added moves to prevent double adding
    moves_name = []

    # Repeatedly asking the user for what moves the new Pokémon has
    while True:
        print("Available moves:\n", formatted_moves)
        selected_move = input("Select move or type 'exit' to exit: ")
        if selected_move == 'exit':
            break

        # Checking to see if inputted move has already been added to moves list
        if selected_move in moves_name:
            print("This move has already been added")

        # Adding move to moves list of new Pokémon
        else:
            try:
                get_index = moves_available.index(selected_move)
                moves.append(moves_obj[get_index])
                moves_name.append(moves_obj[get_index].name)
                print(f"{selected_move} has been successfully added")

            except ValueError:
                print("This is not a valid move")
    return moves


def add_pokemon(pokemon: list, pokemon_obj: list, formatted_moves: str, moves_obj: list, moves_available: list) -> None:
    while True:
        name: str = input("What is the name of this Pokemon? ")

        # checking to see if Pokémon already exists
        if name not in set(pokemon):
            break
        else:
            print("This Pokemon already exists!")
            time.sleep(1)

    health = validate_int_input("How much HP does this Pokemon have?", 1, 300)
    defence = validate_int_input("What is the defence of this Pokemon?", 1, 100)
    speed = validate_int_input("How fast is this Pokemon?", 1, 100)
    moves = allocate_moves_pokemon(formatted_moves, moves_obj, moves_available)

    # creating the new Pokémon object based on user input
    new_pokemon = Pokemon(
        name=name,
        health=health,
        defence=defence,
        speed=speed,
        moves=moves
    )
    # updating available move list with new move
    pokemon.append(new_pokemon.name)
    pokemon_obj.append(new_pokemon)
    return
