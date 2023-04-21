"""
A module for validating a password candidate using re.search() function.

CONSTANTS:
    COMMON_PASSWORDS

FUNCTIONS:
    validate_password()

"""
# Please DO NOT DISTRIBUTE exercise solutions

import re
from is430_unit_test_helpers import assert_equal

def most_common_passwords():
    data_directory_name = 'data'
    infile_name = 'top_100_most_common_passwords.txt'
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r', encoding='utf-8')
    infile_to_list = infile.readlines()

    for i in range(len(infile_to_list)):
        common_passwords.append(infile_to_list[i].strip('\n'))


def validate_password(candidate):
    """
    Validates a candidate password for compliance with organizational standards.

    :param candidate: str value is the proposed new password
    :return: a list of error message strings. Candidate password is valid when list is empty.
    """
    most_common_passwords()
    answer = []   # returning empty list indicates password is valid

    if candidate.lower() in common_password:
        answer.append('Password must not be on the list of common passwords.')

    if len(candidate) < 6:
        answer.append('Password must be at least 6 characters long.')

    if not re.search(r'[A-Z]', candidate):
        answer.append('Password must include at least one upper-case letter (A-Z).')

    if not re.search(r'[a-z]', candidate):
        answer.append('Password must include at least one lower-case letter (a-z).')

    if not re.search(r'[0-9]', candidate):
        answer.append('Password must include at least one digit (0-9).')

    if not re.search(r'[!@#$%^&*]', candidate):
        answer.append('Password must include at least one special character (!@#$%^&*).')

    if re.search(r'opensesame', candidate, re.IGNORECASE):
        answer.append('Password may not contain the word "opensesame" in any case.')

    if re.search(r'password', candidate, re.IGNORECASE):
        answer.append('Password may not contain the word "password" in any case.')

    if re.search(r'secret', candidate, re.IGNORECASE):
        answer.append('Password may not contain the word "secret" in any case.')

    if re.search(r' ', candidate):
        answer.append('Password may not contain a space.')

    downshifted_candidate = candidate.lower()
    if downshifted_candidate in COMMON_PASSWORDS:
        answer.append('Password must not be on the list of common passwords.')

    return answer


def main():
    print('Unit testing output...')

    print('\nTest case 1: password meets all criteria')
    input_password = 'Bc&456'
    expected_result = []
    actual_result = validate_password(input_password)
    assert_equal(expected_result, actual_result)

    print('\nTest case 2: password too short')
    input_password = 'Ab#45'
    expected_result = ['Password must be at least 6 characters long.']
    actual_result = validate_password(input_password)
    assert_equal(expected_result, actual_result)

    print('\nTest case 3: password missing upper case letter')
    input_password = 'ac&456'
    expected_result = ['Password must include at least one upper-case letter (A-Z).']
    actual_result = validate_password(input_password)
    assert_equal(expected_result, actual_result)

    print('\nTest case 4: password missing lower-case letter')
    input_password = 'A*3456'
    expected_result = ['Password must include at least one lower-case letter (a-z).']
    actual_result = validate_password(input_password)
    assert_equal(expected_result, actual_result)

    print('\nTest case 5: password missing special character')
    input_password = 'Aa3456'
    expected_result = ['Password must include at least one special character (!@#$%^&*).']
    actual_result = validate_password(input_password)
    assert_equal(expected_result, actual_result)

    print('\nTest case 6: password contains word opensesame')
    input_password = 'Aa%OpenSesame456'
    expected_result = ['Password may not contain the word "opensesame" in any case.']
    actual_result = validate_password(input_password)
    assert_equal(expected_result, actual_result)

    print('\nTest case 7: password missing multiple of the criteria')
    input_password = '_1234'
    msg_1 = 'Password must be at least 6 characters long.'
    msg_2 = 'Password must include at least one upper-case letter (A-Z).'
    msg_3 = 'Password must include at least one lower-case letter (a-z).'
    msg_4 = 'Password must include at least one special character (!@#$%^&*).'
    expected_result = [msg_1, msg_2, msg_3, msg_4]
    actual_result = validate_password(input_password)
    assert_equal(expected_result, actual_result)

    print('\nTest case 8: password missing digit')
    input_password = 'Aa*bbb'
    expected_result = ['Password must include at least one digit (0-9).']
    actual_result = validate_password(input_password)
    assert_equal(expected_result, actual_result)

    print('\nTest case 9: password contains word password')
    input_password = 'Aa%PaSsWoRd456'
    expected_result = ['Password may not contain the word "password" in any case.']
    actual_result = validate_password(input_password)
    assert_equal(expected_result, actual_result)

    print('\nTest case 10: password contains word secret')
    input_password = 'Aa%SECRET456'
    expected_result = ['Password may not contain the word "secret" in any case.']
    actual_result = validate_password(input_password)
    assert_equal(expected_result, actual_result)

    print('\nTest case 11: password contains a space')
    input_password = 'Bc &56'
    expected_result = ['Password may not contain a space.']
    actual_result = validate_password(input_password)
    assert_equal(expected_result, actual_result)

    print('\nTest case 12: password is on the list of common passwords')
    input_password = 'starwars'
    expected_result = ['Password must include at least one upper-case letter (A-Z).',
                       'Password must include at least one digit (0-9).',
                       'Password must include at least one special character (!@#$%^&*).',
                       'Password must not be on the list of common passwords.']
    actual_result = validate_password(input_password)
    assert_equal(expected_result, actual_result)


if __name__ == '__main__':
    main()
