"""Read an input file. Analyze words on each line, counting numeric characters."""


def main():
    data_directory_name = 'data'
    input_file_name = input(f'Please enter the name of the input file: ')
    infile_path_and_filename = f'{data_directory_name}/{input_file_name}'
    infile = open(infile_path_and_filename, 'r')


    print(f'\nENTRIES:\n{num_string}')
    str_list = line.split()
    num_list = [float(i) for i in str_list]
    print("Output List of numbers is:")
    print(num_list)

    for word in entries:
        entries_count = 0
        entries_count += word.count(entries)
        print(f'"{entries}" contains {entries_count} numeric characters.')

    print(f'\n{line_count} lines were read from file: {input_file_name}')
    print(f'\n{len(entries_count)} entries were processed. ')
    rounded_accumulator = round(accumulator, 3)
    print(f'The accumulated total of the entries was {rounded_accumulator}')

    infile.close()


main()
