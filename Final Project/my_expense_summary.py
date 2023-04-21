"""
Module contains the expense summary class and related test code.
"""

from dataclasses import dataclass
from is430_unit_test_helpers import assert_equal


@dataclass
class ExpenseSummary:
    """A class used to represent an expense summary"""
    category: str
    month: int
    year: int
    us_amount: float
    uk_amount: float
    fr_amount: float

    def calculate_total_amount(self):
        """
        calculates sum of us_amount, uk_amount, and fr_amount

        :return: returns the sum value as a float.
        """
        return self.us_amount + self.uk_amount + self.fr_amount


def main():
    print('Unit testing output follows...')

    print('\nTest Case #1: Test constructor')
    expected_category = 'Fuel'
    expected_month = '1'
    expected_year = '2020'
    expected_us_amount = 72742.79
    expected_uk_amount = 16083.88
    expected_fr_amount = 14365.95
    expense_summary_1 = ExpenseSummary(expected_category, expected_month, expected_year, expected_us_amount, expected_uk_amount, expected_fr_amount)
    assert_equal(expected_category, expense_summary_1.category)
    assert_equal(expected_month, expense_summary_1.month)
    assert_equal(expected_year, expense_summary_1.year)
    assert_equal(expected_us_amount, expense_summary_1.us_amount)
    assert_equal(expected_uk_amount, expense_summary_1.uk_amount)
    assert_equal(expected_fr_amount, expense_summary_1.fr_amount)

    print('\nTest Case #2: Test calculate_total_amount')
    expected_category = 'Fuel'
    expected_month = '1'
    expected_year = '2020'
    expected_us_amount = 72742.79
    expected_uk_amount = 16083.88
    expected_fr_amount = 14365.95
    expected_total_amount = \
        expected_us_amount + expected_uk_amount + expected_fr_amount
    expense_summary_2 = ExpenseSummary(expected_category, expected_month, expected_year, expected_us_amount,
                                       expected_uk_amount, expected_fr_amount)
    assert_equal(expected_total_amount, expense_summary_2.calculate_total_amount())


main()
