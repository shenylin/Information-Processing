"""
Demonstrate flexible user interaction using while.
This program uses a sentinel loop.
It implements the Flexible Integer Adding Machine.
"""


def main():
    print('Welcome to Flexible Integer Adding Machine.\n')
    entry_count = 0
    sum_of_entries = 0
    entry_as_string = input('Please enter an integer value to be added (<Enter> to stop): ')   # priming read

    while entry_as_string != '':
        entry = int(entry_as_string)
        entry_count += 1
        sum_of_entries += entry
        entry_as_string = input('Please enter an integer value to be added (<Enter> to stop): ')

    if entry_count == 0:
        print('\nNo entries were provided.')
    else:
        print(f'\nThe sum of these {entry_count} entries is {sum_of_entries}.')


main()
