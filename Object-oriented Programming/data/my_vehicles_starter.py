"""
Module contains the Vehicle hierarchy of classes and related test code.
"""
# Please DO NOT DISTRIBUTE exercise solutions

from dataclasses import dataclass

from is430_unit_test_helpers import assert_equal, assert_equal_float, PASSED


@dataclass
class Vehicle:
    """A super-class to represent a vehicle"""
    first_name: str
    last_name: str
    street_address_1: str
    street_address_2: str
    city: str
    state: str
    zipcode: str
    make: str
    model: str
    year: int
    color: str
    vehicle_id: str


@dataclass
class Car(Vehicle):
    """A sub-class of Vehicle to represent a car"""
    fuel_type: str

    def determine_annual_registration_fee(self):
        """
        Determines annual registration fee for a car.

        :return: annual_registration_fee (float)
        """
        if self.fuel_type == 'Electric':
            annual_fee = 100.00
        elif self.fuel_type == 'Hybrid':
            annual_fee = 200.00
        elif self.fuel_type == 'Fossil':
            annual_fee = 300.00
        else:
            raise ValueError(f'Expected fuel type of Electric, Hybrid, or Fossil. This value is {self.fuel_type}.')
        return annual_fee


@dataclass
class Truck(Vehicle):
    """A sub-class of Vehicle to represent a truck"""
    gross_weight: int

    def determine_annual_registration_fee(self):
        """
        determines annual registration fee for a truck.

        :return: annual_registration_fee (float)
        """
        if self.gross_weight < 14001:
            annual_fee = 400.00
        else:
            annual_fee = 700.00
        return annual_fee


def main():
    print('Unit testing output follows...')

    # common unit testing variables for all vehicle types
    expected_first_name = 'Maria'
    expected_last_name = 'Gonzalez'
    expected_street_address_1 = '401 Splendid Way'
    expected_street_address_2 = 'Unit A'
    expected_city = 'Glenview'
    expected_state = 'IL'
    expected_zipcode = '60025'
    expected_make = 'American Auto Company'
    expected_model = 'Spirit'
    expected_year = '2020'
    expected_color = 'White'
    expected_vehicle_id = 'VEH1234567890'

    print('\nTest Case #1: Test Vehicle constructor')
    vehicle_1 = Vehicle(expected_first_name,
                 expected_last_name,
                 expected_street_address_1,
                 expected_street_address_2,
                 expected_city,
                 expected_state,
                 expected_zipcode,
                 expected_make,
                 expected_model,
                 expected_year,
                 expected_color,
                 expected_vehicle_id)
    assert_equal(expected_first_name, vehicle_1.first_name)
    assert_equal(expected_last_name, vehicle_1.last_name)
    assert_equal(expected_street_address_1, vehicle_1.street_address_1)
    assert_equal(expected_street_address_2, vehicle_1.street_address_2)
    assert_equal(expected_city, vehicle_1.city)
    assert_equal(expected_state, vehicle_1.state)
    assert_equal(expected_zipcode, vehicle_1.zipcode)
    assert_equal(expected_make, vehicle_1.make)
    assert_equal(expected_model, vehicle_1.model)
    assert_equal(expected_year, vehicle_1.year)
    assert_equal(expected_color, vehicle_1.color)
    assert_equal(expected_vehicle_id, vehicle_1.vehicle_id)

    # common unit testing variables for the Car subtype
    expected_year = 2022
    expected_color = 'Green'
    expected_vehicle_id = 'CAR123456789'

    print('\nTest Case #2: Test Car constructor')
    expected_fuel_type = 'Electric'
    expected_make = 'Nissan'
    expected_model = 'Leaf'
    car_1 = Car(expected_first_name,
                 expected_last_name,
                 expected_street_address_1,
                 expected_street_address_2,
                 expected_city,
                 expected_state,
                 expected_zipcode,
                 expected_make,
                 expected_model,
                 expected_year,
                 expected_color,
                 expected_vehicle_id,
                 expected_fuel_type)
    assert_equal(expected_first_name, car_1.first_name)
    assert_equal(expected_last_name, car_1.last_name)
    assert_equal(expected_street_address_1, car_1.street_address_1)
    assert_equal(expected_street_address_2, car_1.street_address_2)
    assert_equal(expected_city, car_1.city)
    assert_equal(expected_state, car_1.state)
    assert_equal(expected_zipcode, car_1 .zipcode)
    assert_equal(expected_make, car_1.make)
    assert_equal(expected_model, car_1.model)
    assert_equal(expected_year, car_1.year)
    assert_equal(expected_color, car_1.color)
    assert_equal(expected_vehicle_id, car_1.vehicle_id)
    assert_equal(expected_fuel_type, car_1.fuel_type)

    print('\nTest Case #3: Test Car determine_annual_registration_fee, fuel_type = Electric')
    expected_fuel_type = 'Electric'
    expected_make = 'Nissan'
    expected_model = 'Leaf'
    expected_annual_registration_fee = 100.00
    car_2 = Car(expected_first_name,
                 expected_last_name,
                 expected_street_address_1,
                 expected_street_address_2,
                 expected_city,
                 expected_state,
                 expected_zipcode,
                 expected_make,
                 expected_model,
                 expected_year,
                 expected_color,
                 expected_vehicle_id,
                 expected_fuel_type)
    assert_equal_float(expected_annual_registration_fee, car_2.determine_annual_registration_fee(), 0.001)

    print('\nTest Case #4: Test Car determine_annual_registration_fee, fuel_type = Hybrid')
    expected_fuel_type = 'Hybrid'
    expected_make = 'Toyota'
    expected_model = 'Camry Hybrid'
    expected_annual_registration_fee = 200.00
    car_3 = Car(expected_first_name,
                 expected_last_name,
                 expected_street_address_1,
                 expected_street_address_2,
                 expected_city,
                 expected_state,
                 expected_zipcode,
                 expected_make,
                 expected_model,
                 expected_year,
                 expected_color,
                 expected_vehicle_id,
                 expected_fuel_type)
    assert_equal_float(expected_annual_registration_fee, car_3.determine_annual_registration_fee(), 0.001)

    print('\nTest Case #5: Test Car determine_annual_registration_fee, fuel_type = Fossil')
    expected_fuel_type = 'Fossil'
    expected_make = 'Mini'
    expected_model = 'Cooper Countryman All4'
    expected_annual_registration_fee = 300.00
    car_4 = Car(expected_first_name,
                 expected_last_name,
                 expected_street_address_1,
                 expected_street_address_2,
                 expected_city,
                 expected_state,
                 expected_zipcode,
                 expected_make,
                 expected_model,
                 expected_year,
                 expected_color,
                 expected_vehicle_id,
                 expected_fuel_type)
    assert_equal_float(expected_annual_registration_fee, car_4.determine_annual_registration_fee(), 0.001)

    print('\nTest Case #6: Test Car determine_annual_registration_fee, fuel_type = Plutonium')
    expected_fuel_type = 'Plutonium'
    expected_make = 'NASA'
    expected_model = 'Lunar Rover'
    expected_annual_registration_fee = 300.00
    car_4 = Car(expected_first_name,
                 expected_last_name,
                 expected_street_address_1,
                 expected_street_address_2,
                 expected_city,
                 expected_state,
                 expected_zipcode,
                 expected_make,
                 expected_model,
                 expected_year,
                 expected_color,
                 expected_vehicle_id,
                 expected_fuel_type)
    try:
        assert_equal_float(expected_annual_registration_fee, car_4.determine_annual_registration_fee(), 0.001)
        print('Failed. Error was not caught.')
    except ValueError as ve:
        if str(ve) == 'Expected fuel type of Electric, Hybrid, or Fossil. This value is Plutonium.':
            print(PASSED)
        else:
            print(f'Failed. Unexpected error message: {ve}')

    # common unit testing variables for the Truck subtype
    expected_make = 'Ford'
    expected_model = 'F-550'
    expected_year = 2022
    expected_color = 'Grey'
    expected_vehicle_id = 'TRK123456789'
    expected_gross_weight = 14000

    print('\nTest Case #7: Test Truck constructor')
    truck_1 = Truck(expected_first_name,
                      expected_last_name,
                      expected_street_address_1,
                      expected_street_address_2,
                      expected_city,
                      expected_state,
                      expected_zipcode,
                      expected_make,
                      expected_model,
                      expected_year,
                      expected_color,
                      expected_vehicle_id,
                      expected_gross_weight)
    assert_equal(expected_first_name, truck_1.first_name)
    assert_equal(expected_last_name, truck_1.last_name)
    assert_equal(expected_street_address_1, truck_1.street_address_1)
    assert_equal(expected_street_address_2, truck_1.street_address_2)
    assert_equal(expected_city, truck_1.city)
    assert_equal(expected_state, truck_1.state)
    assert_equal(expected_zipcode, truck_1 .zipcode)
    assert_equal(expected_make, truck_1.make)
    assert_equal(expected_model, truck_1.model)
    assert_equal(expected_year, truck_1.year)
    assert_equal(expected_color, truck_1.color)
    assert_equal(expected_vehicle_id, truck_1.vehicle_id)
    assert_equal(expected_gross_weight, truck_1.gross_weight)

    print('\nTest Case #8: Test Truck determine_annual_registration_fee, gross_weight = 14000')
    expected_gross_weight = 14000
    expected_annual_registration_fee = 400.00
    truck_2 = Truck(expected_first_name,
                      expected_last_name,
                      expected_street_address_1,
                      expected_street_address_2,
                      expected_city,
                      expected_state,
                      expected_zipcode,
                      expected_make,
                      expected_model,
                      expected_year,
                      expected_color,
                      expected_vehicle_id,
                      expected_gross_weight)
    assert_equal_float(expected_annual_registration_fee, truck_2.determine_annual_registration_fee(), 0.001)

    print('\nTest Case #9: Test Truck determine_annual_registration_fee, gross_weight = 14001')
    expected_gross_weight = 14001
    expected_annual_registration_fee = 700.00
    truck_2 = Truck(expected_first_name,
                      expected_last_name,
                      expected_street_address_1,
                      expected_street_address_2,
                      expected_city,
                      expected_state,
                      expected_zipcode,
                      expected_make,
                      expected_model,
                      expected_year,
                      expected_color,
                      expected_vehicle_id,
                      expected_gross_weight)
    assert_equal_float(expected_annual_registration_fee, truck_2.determine_annual_registration_fee(), 0.001)


if __name__ == '__main__':
    main()
