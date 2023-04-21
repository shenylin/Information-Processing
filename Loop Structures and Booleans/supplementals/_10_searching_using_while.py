"""
Demonstrate searching using while.
Searches input file for a line containing 3 matching integers.
"""


def main():
    data_directory_name = 'data'
    infile_name = input('Please enter the input filename: ')
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r')
    line_count = 0
    match_found = False
    line = infile.readline()   # priming read

    while line != '' and not match_found:
        line_count += 1
        values_as_string = line.split()
        values = []
        for string_value in values_as_string:
            values.append(int(string_value))
        first, second, third = values
        if first == second == third:   # simple 3-way comparisons are okay.
            match_found = True
            print(f'\nThree matching values of {first} were found on line {line_count:,}.')
        else:
            # placing this read in an else prevents accidentally triggering end-of_file.
            line = infile.readline()

    infile.close()

    if line == '':
        print(f'\nNo matching values were found in {line_count:,} lines.')


main()
