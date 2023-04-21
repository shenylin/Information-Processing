"""Read an input file. Analyze words on each line, counting numeric characters."""


def main():
    numbers = '0123456789'
    data_directory_name = 'data'
    input_file_name = input('Please enter the name of the file to be analyzed: ')
    infile_path_and_filename = f'{data_directory_name}/{input_file_name}'
    infile = open(infile_path_and_filename, 'r')
    line_count = 0

    for line in infile:
        print(f'\nAnalyzing: {line[:-1]}')
        line_count += 1
        words = line.split()

        for word in words:
            numeric_character_count = 0
            for character in numbers:
                numeric_character_count += word.count(character)
            print(f'"{word}" contains {numeric_character_count} numeric characters.')

        print(f'{len(words)} words were analyzed.')

    print(f'\n{line_count} lines were analyzed from the file: {input_file_name}')

    infile.close()


main()