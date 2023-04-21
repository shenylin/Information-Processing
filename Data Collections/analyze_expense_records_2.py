"""Accumulate amounts of qualifying expense records by year. Analyze annually values."""

from statistics import mean
from statistics import median

TARGET_YEAR = 2021
TARGET_CATEGORY = 'Utilities'


def main():
    infile = select_input_file()
    expense_accumulators = [0.00] * 12
    line_count = 0
    qualifying_records = 0

    for line in infile:
        line_count += 1
        if line_count > 1:
            date, category, amount_as_string = line.split(',')
            year, month, day = parse_iso_date(date)
            if year == TARGET_YEAR and category == TARGET_CATEGORY:
                qualifying_records += 1
                expense_accumulators[month - 1] += float(amount_as_string)

    infile.close()
    print_analysis_report(expense_accumulators)
    print(f'\n{line_count:,} lines were read from the input file.')
    print(f'{qualifying_records:,} qualifying expense records were found.')


def parse_iso_date(iso_date):
    year_as_string, month_as_string, day_as_string = iso_date.split('-')
    year = int(year_as_string)
    month = int(month_as_string)
    day = int(day_as_string)
    return year, month, day


def select_input_file():
    data_directory_name = 'data'
    infile_name = input('Please enter the input filename: ')
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r')
    return infile


def print_analysis_report(expense_accumulators):
    print(f'\nSUMMARY OF {TARGET_CATEGORY.upper()} EXPENSES FOR {TARGET_YEAR}')
    print(f'\n{"Month"} {"Amount":>12}')
    for i in range(12):
        print(f'{i + 1:>5}   {expense_accumulators[i]:>12,.2f}')
    mean_value = mean(expense_accumulators)
    print(f'\nThe mean value was {mean_value:,.2f}')
    median_value = median(expense_accumulators)
    print(f'The median value was {median_value:,.2f}')


main()