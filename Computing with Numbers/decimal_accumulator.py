"""Demonstrate quantity of decimal values and the accumulator pattern"""
# decimal_accumulator

from decimal import *


def main():
    accumulator = Decimal('0.00')

    entries_count = int(input('Please enter the quantity of decimal values that you wish to enter: '))

    print()
    for i in range(1, entries_count + 1):
        entry_as_decimal = decimal(input(f'Please enter decimal value {i} of {entries_count}: '))
        accumulator += entry_as_decimal

    print()
    print(f'The accumulated sum of the decimal values is {accumulator}')


main()