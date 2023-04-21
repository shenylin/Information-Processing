"""Validate a new password choice using my_better_password_module."""

from my_better_password_module import validate_password


def main():
    valid_password = False
    password_candidate = input('\nPlease enter a candidate password (<Enter> to cancel): ')

    while password_candidate != '' and not valid_password:
        error_messages = validate_password(password_candidate)
        if len(error_messages) == 0:
            valid_password = True
        else:
            print('\nThis was not an acceptable choice.')
            print('Please correct the following problems:')
            for message in error_messages:
                print(f'    {message}')
            password_candidate = input('\nPlease enter a candidate password (<Enter> to cancel): ')

    if password_candidate == '':
        print('Password change has been canceled.')
    else:
        print('Your new password has been accepted.')


main()