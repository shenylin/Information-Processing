"""Demonstrate using validation function that returns a list of error messages."""


def main():
    print('Guests may ride this attraction if they are at least 6 years old and less than 90 years old.')
    print('Guests may ride this attraction if they weigh at least 50 pounds and less than 300 pounds.')
    age = int(input('\nPlease enter guest\'s age: '))
    weight = int(input('\nPlease enter guest\'s weight (in pounds): '))

    errors = check_guest_qualifications(age, weight)

    if len(errors) == 0:
        print('\nThis guest may ride the attraction.')
    else:
        print('\nThis guest MAY NOT ride the attraction due to the following reasons:')
        for message in errors:
            print(message)


def check_guest_qualifications(age, weight):
    error_messages = []

    if age < 6:
        error_messages.append('Guests must be at least 6 years old.')
    elif age >= 90:
        error_messages.append('Guests must be no more than 89 years old.')

    if weight < 50:
        error_messages.append('Guests must weigh at least 50 pounds.')
    elif weight >= 300:
        error_messages.append('Guests must weigh less than 300 pounds.')

    return error_messages


main()
