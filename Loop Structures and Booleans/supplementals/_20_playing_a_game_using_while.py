"""
Demonstrate playing a game using while.
Implements The Simple Coin Flipping Game.
A player wins when they get HEADS and the other player gets TAILS.
"""

from random import randint

TAILS = 'TAILS'
HEADS = 'HEADS'


def main():
    print('Welcome to The Simple Coin Flipping Game.\n')
    value_a, value_b = play_turn()    # priming turn

    while value_a == value_b:
        value_a, value_b = play_turn()  # if they tie, play again

    if value_a == HEADS:
        print('Player A wins.')
    else:
        print('Player B wins.')


def play_turn():
    a_value = flip_coin()
    b_value = flip_coin()
    print(f'Player A gets {a_value}. Player B gets {b_value}.')
    return a_value, b_value


def flip_coin():
    text_values = [HEADS, TAILS]
    return text_values[randint(0, 1)]


main()
