"""
Demonstrates recovery from bad user integer input using while.
It uses a sentinel loop and catches bad input using a try-except block.
It implements The Usable Integer Adding Machine.
"""


def main():
    print('Welcome to The Usable Integer Adding Machine.\n')
    entry_count = 0
    sum_of_entries = 0
    entry_as_string = input('Please enter an integer value to be added (<Enter> to stop): ')   # priming read

    while entry_as_string != '':
        try:
            entry = int(entry_as_string)
            entry_count += 1
            sum_of_entries += entry
        except ValueError:
            print(f'An integer value was expected. You entered {entry_as_string}')
        entry_as_string = input('Please enter an integer value to be added (<Enter> to stop): ')

    if entry_count == 0:
        print('\nNo entries were provided.')
    else:
        print(f'\nThe sum of these {entry_count} entries is {sum_of_entries}.')


main()
