"""Demonstrate the inline coding of complex decision using nested if-else."""


def main():
    gender = 'female'
    age = 17

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

    print(f'\n{gender} applicant at age {age} pays a {premium:.2f} premium.')


main()
