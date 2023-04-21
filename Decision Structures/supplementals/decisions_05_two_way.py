"""Demonstrate a two-way decision using if-else."""


def main():
    temp = float(input('Please enter today\'s temperature in Fahrenheit: '))
    if temp <= 32.0:
        print('Brrrrr. It is freezing today.')
    else:
        print('Well. At least it is above freezing today!')
    print('Thanks for playing!')


main()
