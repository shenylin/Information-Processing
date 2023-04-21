"""Simulate a 2-player and 3-die game of Going to Boston with a user-chosen number of rounds."""

from random import randint


def main():
    rounds_won_a = 0
    rounds_won_b = 0
    print('Welcome to Going to Boston.\n')
    rounds_to_play = get_number_of_rounds()

    for i in range(1, rounds_to_play + 1):
        round_score_a, round_score_b = play_round(i)
        rounds_won_a += round_score_a
        rounds_won_b += round_score_b

    print_game_results(rounds_won_a, rounds_won_b)


def get_number_of_rounds():
    valid_value = False
    rounds_as_string = input('Please enter the number of rounds to be played (<Enter> to stop): ')
    while rounds_as_string != '' and not valid_value:
        try:
            rounds = int(rounds_as_string)
            if 0 < rounds < 1000:
                valid_value = True
            elif rounds < 0 or rounds > 1000:
                print(f'A value between 0 and 1000 was expected. You entered {rounds}.')
                rounds_as_string = input('Please enter the number of rounds to be played (<Enter> to stop): ')
            elif rounds == 0:
                print('No rounds were requested. Come play again soon.')
                break
            else:
                print(f'An integer was expected. You entered {rounds_as_string}.')
                rounds_as_string = input('Please enter the number of rounds to be played (<Enter> to stop): ')
        except ValueError:
            print(f'An integer was expected. You entered {rounds_as_string}.')
            rounds_as_string = input('Please enter the number of rounds to be played (<Enter> to stop): ')
    if rounds_as_string == '':
        rounds = 0
        print('No rounds were requested. Come play again soon.')
    return rounds


def play_round(round_number):
    print(f'\nPlaying Round {round_number}:')
    turn_score_a = play_turn('A')
    print(f'==>Player A\'s turn score is {turn_score_a}')
    turn_score_b = play_turn('B')
    print(f'==>Player B\'s turn score is {turn_score_b}')
    if turn_score_a > turn_score_b:
        print('Player A wins the round!')
        a_round_score = 1
        b_round_score = 0
    elif turn_score_a < turn_score_b:
        print('Player B wins the round!')
        a_round_score = 0
        b_round_score = 1
    else:
        print('The players tie the round.')
        a_round_score = 0
        b_round_score = 0
    return a_round_score, b_round_score


def play_turn(player_name):
    print(f'Player {player_name}\'s turn...')
    rolls = roll_dice(3)
    print(f'Player {player_name} rolls {rolls} and keeps {max(rolls)}.')
    rolls = roll_dice(2)
    print(f'Player {player_name} rolls {rolls} and keeps {max(rolls)}.')
    rolls = roll_dice(1)
    print(f'Player {player_name} rolls and keeps {max(rolls)}.')
    choice = choose_value(rolls)
    return choice


def roll_dice(number_of_dice):
    rolls = []
    for i in range(number_of_dice):
        rolls.append(roll_die())
    return rolls


def roll_die():
    return randint(1, 6)


def choose_value(rolls):
    sorted_rolls = sorted(rolls, reverse=True)
    choice = sorted_rolls[0]
    return choice


def print_game_results(a_rounds_won, b_rounds_won):
    print('\nGame Results:')
    if a_rounds_won != 0 and a_rounds_won > 1:
        print(f'Player A has won {a_rounds_won} rounds.')
    elif a_rounds_won != 0 and a_rounds_won == 1:
        print(f'Player A has won {a_rounds_won} round.')
    if b_rounds_won != 0 and b_rounds_won > 1:
        print(f'Player B has won {b_rounds_won} rounds.')
    elif b_rounds_won != 0 and b_rounds_won == 1:
        print(f'Player B has won {b_rounds_won} round.')

    if a_rounds_won > b_rounds_won:
        print('Player A wins the game!')
    elif a_rounds_won < b_rounds_won:
        print('Player B wins the game!')
    else:
        print('The players tie the game.')


main()
