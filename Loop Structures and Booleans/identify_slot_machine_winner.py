"""
Demonstrate searching using while.
Searches input file for a line containing 3 matching integers.
"""


def main(string_list=list):
    data_directory_name = 'data'
    infile_name = input('Please enter the input filename: ')
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r')
    line_count = 0
    match_found = False
    line = infile.readline()   # priming read

    while line != '' and not match_found:
        line_count += 1
        color_list = line.split()
        red_count = color_list.count('Red')
        blue_count = color_list.count('Blue')
        values = []

        for string_value in color_list:
            values.append(string_value)
        if red_count == 3 and blue_count == 2:
            match_found = True
            print(f'\nWinner found on line {line_count}: {line}')
        else:
            # placing this read in an else prevents accidentally triggering end-of_file.
            line = infile.readline()

    infile.close()

    if line == '':
        print(f'\nNo winning slot values found.')
        print(f'{line_count} lines read from {infile_name}')


main()
