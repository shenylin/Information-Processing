"""Print a report of company-wide expense records from a file in two different sort orders."""

from my_expense_summary import ExpenseSummary


def main():
    expenses, category, year = get_expenses()

    sorted(expenses, key=by_month)
    print_report(expenses, 'BY MONTH', category, year)

    expenses.sort(key=by_total_amount, reverse=True)
    print_report(expenses, 'BY DESCENDING TOTAL AMOUNT', category, year)


def get_expenses():
    data_directory_name = 'data'
    infile_name = input('Please enter input file name: ')
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r', encoding='utf-8')
    my_expenses = []
    lines = infile.readlines()[1:]
    if not infile.read(1):
        category, year = '', 0
    for line in lines:
        category, month, year, us_amount, uk_amount, fr_amount = line.split(',')
        my_expenses.append(
            ExpenseSummary(category, month, year, float(us_amount), float(uk_amount), float(fr_amount))
        )
    infile.close()
    return my_expenses, category, year


def print_report(these_expenses, report_title, category, year):
    print()
    print()
    print(f'{"COMBINED OPERATIONS":^65}')
    print(f'{" ":<12}SUMMARY OF {category.upper()} EXPENSE AMOUNTS FOR {year}')
    print(f'{report_title:^65}')
    print()
    print(f'{"Month":>6}{"US Amount":>15}{"UK Amount":>15}{"FR Amount":>15}{"Total Amount":>15}')
    print(f'{" ":>6}{"(USD)":>15}{"(USD)":>15}{"(USD)":>15}{"(USD)":>15}')
    total_us = total_uk = total_fr = total_total = 0
    for expense in these_expenses:
        total_us += expense.us_amount
        total_uk += expense.uk_amount
        total_fr += expense.fr_amount
        total_total += expense.calculate_total_amount()
        print(f'{expense.month:>6}'
              f'{expense.us_amount:>15,.2f}'
              f'{expense.uk_amount:>15,.2f}'
              f'{expense.fr_amount:>15,.2f}'
              f'{expense.calculate_total_amount():>15,.2f}')
    print(f'{"Total":>6}{total_us:>15,.2f}{total_uk:>15,.2f}{total_fr:>15,.2f}{total_total:>15,.2f}')


def by_month(an_expense_instance):
    return an_expense_instance.month


def by_total_amount(an_expense_instance):
    return an_expense_instance.calculate_total_amount()


main()
