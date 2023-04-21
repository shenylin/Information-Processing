"""Demonstrate mixed type division and the accumulator pattern"""
# remainder_accumulator


def main():
    accumulator = 0.0

    pairs_to_collect = int(input('Please enter the quantity of number pairs that you wish to enter: '))

    for i in range(1, pairs_to_collect + 1):
        print(f'Now collecting number pair {i} of {pairs_to_collect}... ')
        dividend = float(input('Please enter a float value for the dividend: '))
        divisor = int(input('Please enter an integer value for the divisor: '))

        quotient = dividend / divisor
        print(f'The quotient is {quotient:.3f}')
        accumulator = quotient * pairs_to_collect
        print()

    rounded_accumulator = round(accumulator, 3)
    print(f'The accumulated sum of the quotients is {rounded_accumulator}')


main()