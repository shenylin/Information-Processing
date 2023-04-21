"""Demonstrate detection of bad input with graceful exit."""

from sys import exit


def main():
    try:
        entry_as_string = input('Please enter an integer: ')
        some_integer = int(entry_as_string)
        print(f'\nYou have entered the integer {some_integer}.')
    except ValueError:
        print(f'\nAn integer was expected. You entered "{entry_as_string}".')
        print('Program is ending. Please run it again with proper input.')
        exit()

    print('Thanks for playing.')


main()
