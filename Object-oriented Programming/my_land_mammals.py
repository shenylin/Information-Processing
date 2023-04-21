"""
Module contains the land mammal class and related test code.
"""

from dataclasses import dataclass
from is430_unit_test_helpers import assert_equal


@dataclass
class LandMammal:
    """A class used to represent a land mammal"""
    LandMammal_name: str
    minimum_mass_in_pounds: int
    maximum_mass_in_pounds: int

    def calculate_range_of_mass_in_pounds(self):
        """
        calculates range of mass in pounds

        :return: returns the maximum value minus the minimum value as an int.
        """
        return self.maximum_mass_in_pounds - self.minimum_mass_in_pounds


def main():
    print('Unit testing output follows...')

    # common variables for LandMammal class unit tests
    expected_land_mammal_name = 'African elephant'
    expected_minimum_mass_in_pounds = 10000
    expected_maximum_mass_in_pounds = 24000

    print('\nTest Case #1: Test constructor')
    land_mammal_1 = LandMammal(expected_land_mammal_name, expected_minimum_mass_in_pounds, expected_maximum_mass_in_pounds)
    assert_equal(expected_land_mammal_name, land_mammal_1.LandMammal_name)
    assert_equal(expected_minimum_mass_in_pounds, land_mammal_1.minimum_mass_in_pounds)
    assert_equal(expected_maximum_mass_in_pounds, land_mammal_1.maximum_mass_in_pounds)

    print('\nTest Case #2: Test calculate_range_of_mass_in_pounds method')
    expected_range_of_mass_in_pounds = 14000
    land_mammal_2 = LandMammal(expected_land_mammal_name, expected_minimum_mass_in_pounds, expected_maximum_mass_in_pounds)
    assert_equal(expected_range_of_mass_in_pounds, land_mammal_2.calculate_range_of_mass_in_pounds())


if __name__ == '__main__':
    main()
