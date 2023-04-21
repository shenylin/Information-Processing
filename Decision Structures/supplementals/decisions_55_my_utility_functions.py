"""A module containing commonly used functions."""

METERS_TO_INCHES_FACTOR = 39.370
MILES_TO_KILOMETERS_FACTOR = 1.609344


def miles_to_kilometers(miles):
    return miles * MILES_TO_KILOMETERS_FACTOR


def meters_to_inches(meters):
    return meters * METERS_TO_INCHES_FACTOR


def main():
    passed = True
    if miles_to_kilometers(1.0) != MILES_TO_KILOMETERS_FACTOR:
        passed = False
    if meters_to_inches(1.0) != METERS_TO_INCHES_FACTOR:
        passed = False
    if passed:
        print('\nAll tests for decisions_55_my_utility_functions have passed.')
    else:
        print('\nSome tests for decisions_55_my_utility_functions have failed.')


if __name__ == '__main__':
    main()
