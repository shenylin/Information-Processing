"""Demonstrate a simple lookup refactored to a function."""


def main():
    place = int(input('Please enter place finished (1, 2, 3...): '))

    ribbon = lookup_ribbon(place)
    print()
    print('Ribbon Awarded:', ribbon)


def lookup_ribbon(place):
    if place == 1:
        ribbon = 'Blue'
    elif place == 2:
        ribbon = 'Red'
    elif place == 3:
        ribbon = 'Orange'
    elif place == 4:
        ribbon = 'Gold'
    elif place == 5:
        ribbon = 'Green'
    elif place == 6:
        ribbon = 'Purple'
    elif place > 6:
        ribbon = 'White'
    else:
        ribbon = 'ERROR - Place must be greater than zero.'
    return ribbon


main()
