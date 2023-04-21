"""
Select and summarizes qualifying France expense records.

Prints report.
Writes summarized file.
"""

EUROS_TO_DOLLARS_CONVERSION_FACTOR = 1.1043


def main():
    target_year = 2020
    target_category = 'Fuel'
    data_directory = 'data'
    input_filename = 'fr_expense_records.txt'
    output_filename = 'fr_summarized_target_expenses.txt'
    do_fr_select_and_summarize(target_year,
                               target_category,
                               data_directory,
                               input_filename,
                               output_filename)


def do_fr_select_and_summarize(target_year,
                               target_category,
                               data_directory,
                               input_filename,
                               output_filename):

    expense_accumulators = select_and_accumulate_qualifying_records(data_directory,
                                                                    input_filename,
                                                                    target_category,
                                                                    target_year)

    print_analysis_report(expense_accumulators, target_category, target_year)
    create_summary_file(expense_accumulators,
                        data_directory,
                        output_filename,
                        target_category,
                        target_year)


def select_and_accumulate_qualifying_records(data_directory, input_filename, target_category, target_year):
    infile_path_and_name = f'{data_directory}/{input_filename}'
    infile = open(infile_path_and_name, 'r', encoding='utf-8')
    expense_accumulators = [0.00] * 12
    line_count = 0
    qualifying_records = 0
    for line in infile:
        line_count += 1
        if line_count > 1:
            date, category, amount_as_string = line.split(',')
            day, month, year = parse_fr_date(date)
            if year == target_year and category == target_category:
                qualifying_records += 1
                expense_accumulators[month - 1] += float(amount_as_string)*EUROS_TO_DOLLARS_CONVERSION_FACTOR
    infile.close()
    print(f'\n{line_count:,} lines were read from {input_filename}.')
    print(f'{qualifying_records:,} qualifying expense records were accumulated.')
    return expense_accumulators


def parse_fr_date(fr_date):
    day_as_string, month_as_string, year_as_string = fr_date.split('/')
    day = int(day_as_string)
    month = int(month_as_string)
    year = int(year_as_string)
    return day, month, year


def print_analysis_report(expense_accumulators, the_target_category, the_target_year):
    print('\n\nFRENCH OPERATIONS')
    print(f'SUMMARY OF {the_target_category.upper()} EXPENSES FOR {the_target_year}')
    print(f'\n{"Month"}    {"Amount (USD)":>12}')
    for i in range(12):
        print(f'{i + 1:>5}   {expense_accumulators[i]:>12,.2f}')


def create_summary_file(the_expense_accumulators,
                        the_data_directory,
                        the_output_filename,
                        the_target_category,
                        the_target_year):
    outfile_path_and_name = f'{the_data_directory}/{the_output_filename}'
    outfile = open(outfile_path_and_name, 'w', encoding='utf-8')
    print('Country, Expense Category,Month,Year,Amount (USD)', file=outfile)

    for month in range(1, 13):
        content = f'{"FR"},{the_target_category},{month},{the_target_year}, {the_expense_accumulators[month - 1]:.2f}'
        print(content, file=outfile)

    outfile.close()
    print(f'\n\nSummary file was created as {the_output_filename}.')


if __name__ == '__main__':
    main()












