"""
Demonstrate playing a game using while.
Implements The Simple Coin Flipping Game.
A player wins when they get HEADS and the other player gets TAILS.
"""

from random import randint

ROCK = 'ROCK'
PAPER = 'PAPER'
SCISSORS = 'SCISSORS'


def main():
    print('Welcome to The Rock-Paper-Scissors Game.\n')
    value_a, value_b = play_turn()    # priming turn

    while value_a == value_b:
        value_a, value_b = play_turn()  # if they tie, play again

    if value_a == ROCK:
        if value_b == SCISSORS:
            print('Player A wins.')
        else:
            print('Player B wins.')

    if value_a == SCISSORS:
        if value_b == PAPER:
            print('Player A wins.')
        else:
            print('Player B wins.')

    if value_a == PAPER:
        if value_b == ROCK:
            print('Player A wins.')
        else:
            print('Player B wins.')


def play_turn():
    a_value = rock_paper_scissors()
    b_value = rock_paper_scissors()
    print(f'Player A throws {a_value}. Player B throws {b_value}.')
    return a_value, b_value


def rock_paper_scissors():
    text_values = [ROCK, PAPER, SCISSORS]
    return text_values[randint(0, 2)]


main()
