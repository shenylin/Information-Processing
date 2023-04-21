"""Demonstrate a basic multi-way decision using if-elif-else."""


def main():
    temp = float(input('Please enter today\'s temperature in Fahrenheit: '))

    if temp <= 0.0:
        print('Watch Out. It is Chicago cold today.')
    elif temp <= 32.0:
        print('Brrrrr. It is freezing today.')
    else:
        print('Well. At least it is above freezing today!')
    print('Thanks for playing!')


main()
