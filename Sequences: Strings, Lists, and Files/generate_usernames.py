"""From a file of natural-order names, generate a file of usernames."""


def main():
    line_count = 0
    data_directory_name = 'data'
    input_file_name = input('Please enter the name of the file containing names: ')
    infile_path_and_filename = f'{data_directory_name}/{input_file_name}'
    infile = open(infile_path_and_filename, 'r')
    output_file_name = 'username_assignments.txt'
    outfile_path_and_filename = f'{data_directory_name}/{output_file_name}'
    outfile = open(outfile_path_and_filename, 'w', encoding='utf-8')

    for line in infile:
        line_count += 1
        first_name, last_name = line.split()

        first_name = f'{first_name}'
        username_first_name = first_name[0].lower()

        last_name = f'{last_name}'
        username_last_name = last_name[0:6].lower()

        user_name = f'{first_name} {last_name},{username_first_name}{username_last_name}'
        print(user_name, file=outfile)

    print(f'\n{line_count} lines were processed from input file: {input_file_name}')
    print(f'\nCreated username assignments file as: {output_file_name}')

    infile.close()
    outfile.close()


main()
