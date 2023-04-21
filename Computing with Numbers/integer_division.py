# integer_division_2


def main():
    dividend = int(input('Please enter an integer for the dividend: '))
    divisor = int(input('Please enter an integer for the divisor: '))

    quotient = dividend // divisor
    remainder = dividend % divisor

    print()
    print(f'The quotient is {quotient} and the remainder is {remainder}.')


main()