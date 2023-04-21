"""
Demonstrate complex decision using nested if-else factored into a function.
Demonstrate a more automated approach to unit testing.
"""


def main():
    print(determine_premium(18, 'male') == 200.00)
    print(determine_premium(24, 'male') == 200.00)
    print(determine_premium(25, 'male') == 160.00)
    print(determine_premium(26, 'male') == 160.00)

    print(determine_premium(18, 'female') == 100.00)
    print(determine_premium(24, 'female') == 100.00)
    print(determine_premium(25, 'female') == 70.00)
    print(determine_premium(26, 'female') == 70.00)

    print(determine_premium(29, 'non-binary') == 70.00)


def determine_premium(age, gender):
    if gender == 'male':
        if age < 25:
            premium = 200.00
        else:
            premium = 160.00
    elif gender == 'female':
        if age < 25:
            premium = 100.00
        else:
            premium = 70.00
    else:
        raise ValueError(f'Gender coded as "{gender}". We were not ready for this. Please contact the IT department!')

    return premium


main()
