"""Demonstrate using try-except block to detect exception raised in called code."""

from sys import exit


def main():
    try:
        some_integer = get_my_integer_from_user()
        print(f'You have entered the integer {some_integer}.')
    except ValueError:
        print(f'\nAn integer was expected.')
        print('Program is ending. Please run it again with proper input.')
        exit()
    finally:
        print('Let''s put our toys away before we leave.')

    print('Thanks for playing.')


def get_my_integer_from_user():
    some_integer = int(input('Please enter an integer: '))
    return some_integer


main()
