"""Reads US, UK, and FR summarized expense records and joins them into a single file."""


def main():
    data_directory = 'data'
    us_input_filename = 'us_summarized_target_expenses.txt'
    uk_input_filename = 'uk_summarized_target_expenses.txt'
    fr_input_filename = 'fr_summarized_target_expenses.txt'
    output_filename = 'joined_summarized_target_expenses.txt'
    do_join_selected_summarized_expenses(data_directory,
                                         us_input_filename,
                                         uk_input_filename,
                                         fr_input_filename,
                                         output_filename)


def do_join_selected_summarized_expenses(data_directory,
                                         us_input_filename,
                                         uk_input_filename,
                                         fr_input_filename,
                                         output_filename):

    us_infile, uk_infile, fr_infile, outfile = open_all_files(data_directory,
                                                              us_input_filename,
                                                              uk_input_filename,
                                                              fr_input_filename,
                                                              output_filename)
    us_line, uk_line, fr_line = get_next_lines(fr_infile, uk_infile, us_infile)
    if us_line == '' or uk_line == '' or fr_line == '':
        raise ValueError('One or more input files are empty.')
    print('Expense Category,Month,Year,US Amount (USD), UK Amount (USD), FR Amount (USD)', file=outfile)
    outfile_line_count = 0
    us_line, uk_line, fr_line = get_next_lines(fr_infile, uk_infile, us_infile)

    while us_line != '' and uk_line != '' and fr_line != '':
        us_country, us_category, us_month, us_year, us_amount = us_line[:-1].split(',')
        uk_country, uk_category, uk_month, uk_year, uk_amount = uk_line[:-1].split(',')
        fr_country, fr_category, fr_month, fr_year, fr_amount = fr_line[:-1].split(',')
        if not(us_category == uk_category == fr_category):
            raise ValueError('Categories of records in input files do not agree.')
        if not(us_month == uk_month == fr_month):
            raise ValueError('Months of records in input files do not agree.')
        if not(us_year == uk_year == fr_year):
            raise ValueError('Years of records in input files do not agree.')
        content = f'{us_category},{us_month},{us_year},{us_amount},{uk_amount},{fr_amount}'
        print(content, file=outfile)
        outfile_line_count += 1
        us_line, uk_line, fr_line = get_next_lines(fr_infile, uk_infile, us_infile)

    close_all_files(fr_infile, outfile, uk_infile, us_infile)
    print(f'\n{outfile_line_count} joined expense summary records were written to {output_filename}.')


def open_all_files(data_directory,
                   us_input_filename,
                   uk_input_filename,
                   fr_input_filename,
                   output_filename):
    us_infile_path_and_name = f'{data_directory}/{us_input_filename}'
    us_infile = open(us_infile_path_and_name, 'r', encoding='utf-8')
    uk_infile_path_and_name = f'{data_directory}/{uk_input_filename}'
    uk_infile = open(uk_infile_path_and_name, 'r', encoding='utf-8')
    fr_infile_path_and_name = f'{data_directory}/{fr_input_filename}'
    fr_infile = open(fr_infile_path_and_name, 'r', encoding='utf-8')
    outfile_path_and_name = f'{data_directory}/{output_filename}'
    outfile = open(outfile_path_and_name, 'w', encoding='utf-8')
    return us_infile, uk_infile, fr_infile, outfile


def get_next_lines(fr_infile, uk_infile, us_infile):
    us_line = us_infile.readline()
    uk_line = uk_infile.readline()
    fr_line = fr_infile.readline()
    return us_line, uk_line, fr_line


def close_all_files(fr_infile, outfile, uk_infile, us_infile):
    us_infile.close()
    uk_infile.close()
    fr_infile.close()
    outfile.close()


if __name__ == '__main__':
    main()
