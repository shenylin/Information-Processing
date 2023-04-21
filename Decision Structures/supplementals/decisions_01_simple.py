"""Demonstrate a simple decision using if."""


def main():
    temp = float(input('Please enter today\'s temperature in Fahrenheit: '))
    if temp <= 32.0:
        print('Brrrrr. It is freezing today.')

    print('Thanks for playing!')


main()
