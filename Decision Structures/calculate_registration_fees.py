"""
Demonstrate complex decision using nested if-else factored into a function.
Demonstrate a more automated approach to unit testing.
"""
# vehicle annual registration fee. Car = 125.00 if under 3000, otherwise 200.00
# vehicle annual registration fee. Truck = 250.00 if under 4000, otherwise 350.00


def main():
    print(determine_annual_registration_fee(2000, 'Car') == 125.00)
    print(determine_annual_registration_fee(3000, 'Car') == 200.00)
    print(determine_annual_registration_fee(3001, 'Car') == 200.00)
    print(determine_annual_registration_fee(4000, 'Car') == 200.00)

    print(determine_annual_registration_fee(3999, 'Truck') == 250.00)
    print(determine_annual_registration_fee(4000, 'Truck') == 350.00)
    print(determine_annual_registration_fee(4001, 'Truck') == 350.00)
    print(determine_annual_registration_fee(5000, 'Truck') == 350.00)

    print(determine_annual_registration_fee(1999, 'motorcycle') == 100.00)


def determine_annual_registration_fee(weight, vehicle_type):
    if vehicle_type == 'Car':
        if weight < 3000:
            annual_fee = 125.00
        else:
            annual_fee = 200.00
    elif vehicle_type == 'Truck':
        if weight < 4000:
            annual_fee = 250.00
        else:
            annual_fee = 350.00
    else:
        raise ValueError(f' "motorcycle" is not a recognized vehicle-type.')

    return annual_fee


main()
