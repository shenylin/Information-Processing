"""Convert a measurement in pounds to a measurement in stones."""


def main():
    stones = eval(input("Please enter measurement in stones:"))

    pounds = stones * 0.0714286

    print('Measure in pounds:', pounds)


main()