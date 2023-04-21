"""Demonstrate detection of bad input with graceful exit."""

from sys import exit


def main():
    intro()
    entry_as_string = ''

    for i in range(5):
        try:
            entry_as_string = input('\nPlease enter an integer: ')
            some_integer = int(entry_as_string)
            print(f'\nYou have entered the integer {some_integer}.')
        except ValueError:
            print(f'\nAn integer was expected. You entered "{entry_as_string}".')
            print('Program is ending. Please run it again with proper input.')
            exit()

    print('\nThanks for playing.')


def intro():
    print('This program prompts you for 5 integers.')
    print('Valid integer inputs are echoed back to the user.')
    print('Invalid inputs cause an error message and a graceful exit.')


main()
