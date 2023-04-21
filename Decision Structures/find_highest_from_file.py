"""Demonstrate general approach to finding the highest value in a sequence."""
"""From a file of random integers between -100_000 and 100_000, find the highest value."""


def main():
    data_directory_name = 'data'
    input_file_name = input(f'Please enter the name of the file containing integer values: ')
    infile_path_and_filename = f'{data_directory_name}/{input_file_name}'
    infile = open(infile_path_and_filename, 'r')
    value_count = 0
    highest_so_far = -999_999    # lower than any value to be found in the file

    for line in infile:
        value_count += 1
        this_integer = int(line)
        if this_integer > highest_so_far:
            highest_so_far = this_integer

    infile.close()

    if input_file_name.startswith("empty"):
        print(f'\nThe input file was empty. No values could be analyzed.')
    else:
        print(f'\nThe input file contained {value_count} entries.')
        print(f'The highest value was {highest_so_far}.')


main()
