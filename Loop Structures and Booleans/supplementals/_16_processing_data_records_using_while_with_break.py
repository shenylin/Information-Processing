"""
Demonstrate processing data records using while and break statement.
Transforms records with names in natural order to records with names in sort order.
Strict structured programming advocates do NOT use the break statement.
"""


def main():
    data_directory_name = 'data'
    infile_name = input('Please enter the input filename: ')
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r')
    outfile_name = 'sort_order_' + infile_name
    outfile_path_and_name = f'{data_directory_name}/{outfile_name}'
    outfile = open(outfile_path_and_name, 'w', encoding='utf-8')
    line_count = 0

    while True:
        line = infile.readline()
        if line == '':
            # break statement jumps out of the loop immediately
            break
        line_count += 1
        first_name, last_name = line.split()
        content = f'{last_name}, {first_name}'
        print(content, file=outfile)

    infile.close()

    print(f'\n{line_count} records were read from {infile_name}')
    print(f'{line_count} records were written to {outfile_name}')


main()
