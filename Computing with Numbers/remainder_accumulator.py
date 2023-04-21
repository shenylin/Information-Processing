"""Demonstrate integer division and the accumulator pattern"""
# remainder_accumulator


def main():
    accumulator = 1
    pairs_to_collect = int(input('Please enter the quantity of integer pairs that you wish to enter: '))

    for i in range(1, pairs_to_collect + 1):
        print(f'Now collecting integer pair {i} of {pairs_to_collect}... ')
        dividend = int(input('Please enter an integer for the dividend: '))
        divisor = int(input('Please enter an integer for the divisor: '))

        remainder = dividend % divisor
        print(f'The remainder is {remainder}.')
        accumulator = remainder * pairs_to_collect
        print()

    print(f'The accumulated sum of the remainders is {accumulator}.')


main()