"""
Module contains the State class and related test code.
"""

from dataclasses import dataclass
from is430_unit_test_helpers import assert_equal, assert_equal_float


@dataclass
class State:
    """A class used to represent a state"""
    state_name: str
    land_area_in_square_miles: float
    water_area_in_square_miles: float

    def calculate_total_area_in_square_miles(self):
        """
        calculates total area in square miles

        :return: total_area_in_square_miles (float)
        """
        return self.land_area_in_square_miles + self.water_area_in_square_miles


def main():
    print('Unit testing output follows...')

    # common variables for State class unit tests
    expected_state_name = 'Alaska'
    expected_land_area_in_square_miles = 570640.95
    expected_water_area_in_square_miles = 94743.10

    print('\nTest Case #1: Test constructor')
    state_1 = State(expected_state_name, expected_land_area_in_square_miles, expected_water_area_in_square_miles)
    assert_equal(expected_state_name, state_1.state_name)
    assert_equal(expected_land_area_in_square_miles, state_1.land_area_in_square_miles)
    assert_equal(expected_water_area_in_square_miles, state_1.water_area_in_square_miles)

    print('\nTest Case #2: Test calculate_total_area_in_square_miles method')
    expected_total_area_in_square_miles = 665384.05
    state_2 = State(expected_state_name, expected_land_area_in_square_miles, expected_water_area_in_square_miles)
    assert_equal_float(expected_total_area_in_square_miles, state_2.calculate_total_area_in_square_miles(), 0.001)


if __name__ == '__main__':
    main()
