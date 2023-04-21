"""Demonstrate an extended multi-way decision using if-elif-else."""


def main():
    temp = float(input('Please enter today\'s temperature in Fahrenheit: '))
    if temp <= -50.0:
        print('Careful.  It is arctic cold today.')
    elif temp <= -20.0:
        print('Watch Out. It is Minnesota cold today.')
    elif temp <= 0.0:
        print('Watch Out. It is Chicago cold today.')
    elif temp <= 32.0:
        print('Brrrrr. It is freezing today.')
    elif temp < 40.0:
        print('Well. At least it is above freezing today!')
    elif temp <= 70.0:
        print('We can expect to see undergraduates wearing sandals today!')
    elif temp < 80.0:
        print('What a beautiful day!')
    else:
        print('Can you believe how hot it is today?')
    print('Thanks for playing!')


main()
