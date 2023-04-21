"""Demonstrate multi-faceted validation using ifs."""


def main():
    print('Guests may ride this attraction if they are at least 6 years old and less than 90 years old.')
    print('Guests may ride this attraction if they weigh at least 50 pounds and less than 300 pounds.')
    age = int(input('\nPlease enter guest\'s age: '))
    weight = int(input('\nPlease enter guest\'s weight (in pounds): '))

    guest_qualified = True

    if age < 6:
        guest_qualified = False
    elif age >= 90:
        guest_qualified = False

    if weight < 50:
        guest_qualified = False
    elif weight >= 300:
        guest_qualified = False

    if guest_qualified:
        print('\nThis guest may ride the attraction.')
    else:
        print('\nThis guest MAY NOT ride the attraction.')


main()
