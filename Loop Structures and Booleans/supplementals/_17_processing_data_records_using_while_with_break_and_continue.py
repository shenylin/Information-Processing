"""
Demonstrate processing data records using while with break and continue to implement optional behavior.
Transforms a subset of the records with names in natural order to records with names in sort order.
While some programmers do use the break statement, most programmers do NOT use the continue statement.
"""


def main():
    data_directory_name = 'data'
    infile_name = input('Please enter the input filename: ')
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r')
    outfile_name = 'sort_order_' + infile_name
    outfile_path_and_name = f'{data_directory_name}/{outfile_name}'
    outfile = open(outfile_path_and_name, 'w', encoding='utf-8')
    input_line_count = 0
    output_line_count = 0

    while True:
        line = infile.readline()
        if line == '':
            # break statement jumps out of the loop immediately
            break
        input_line_count += 1
        if input_line_count <= 50:
            # continue statement causes the remaining statements in the loop to be skipped.
            # unlike the break statement, the loop does continue execution.
            continue
        first_name, last_name = line.split()
        content = f'{last_name}, {first_name}'
        print(content, file=outfile)
        output_line_count += 1

    infile.close()

    print(f'\n{input_line_count} records were read from {infile_name}')
    print(f'{output_line_count} records were written to {outfile_name}')


main()
