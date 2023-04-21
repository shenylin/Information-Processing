"""Print vehicle registration invoices for cars, trucks and motorcycles."""


from my_vehicles import Car, Truck, Motorcycle


def main():
    vehicles = get_vehicles()
    vehicles.sort(key=by_first_name)
    vehicles.sort(key=by_last_name)
    vehicles.sort(key=by_city)
    print_invoices(vehicles)


def get_vehicles():
    data_directory_name = 'data'
    infile_name = input('Please enter the input filename: ')
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r', encoding='utf-8')
    my_vehicles = []
    for line in infile:
        if line.startswith('Car'):
            vehicle = construct_car_instance(line)
        elif line.startswith('Truck'):
            vehicle = construct_truck_instance(line)
        elif line.startswith('Motorcycle'):
            vehicle = construct_motorcycle_instance(line)
        else:
            raise ValueError(f'Car, Truck or Motorcycle was expected. This line starts with: {line[0:10]}')
        my_vehicles.append(vehicle)

    infile.close()
    return my_vehicles


def construct_car_instance(line):
    line = line.strip()
    data_fields = line.split(',')
    vehicle_type, first_name, last_name, street_address_1, street_address_2 = data_fields[0:5]
    city, state, zipcode, make, model, year, color, vehicle_id, fuel_type = data_fields[5:]
    vehicle = Car(first_name,
                  last_name,
                  street_address_1,
                  street_address_2,
                  city,
                  state,
                  zipcode,
                  make,
                  model,
                  int(year),
                  color,
                  vehicle_id,
                  fuel_type)
    return vehicle


def construct_truck_instance(line):
    line = line.strip()
    data_fields = line.split(',')
    vehicle_type, first_name, last_name, street_address_1, street_address_2 = data_fields[0:5]
    city, state, zipcode, make, model, year, color, vehicle_id, gross_weight = data_fields[5:]
    vehicle = Truck(first_name,
                    last_name,
                    street_address_1,
                    street_address_2,
                    city,
                    state,
                    zipcode,
                    make,
                    model,
                    int(year),
                    color,
                    vehicle_id,
                    int(gross_weight))
    return vehicle


def construct_motorcycle_instance(line):
    line = line.strip()
    data_fields = line.split(',')
    vehicle_type, first_name, last_name, street_address_1, street_address_2 = data_fields[0:5]
    city, state, zipcode, make, model, year, color, vehicle_id, displacement_in_ccs = data_fields[5:]
    vehicle = Motorcycle(first_name,
                    last_name,
                    street_address_1,
                    street_address_2,
                    city,
                    state,
                    zipcode,
                    make,
                    model,
                    int(year),
                    color,
                    vehicle_id,
                    int(displacement_in_ccs))
    return vehicle


def by_first_name(vehicle_instance):
    return vehicle_instance.first_name


def by_last_name(vehicle_instance):
    return vehicle_instance.last_name


def by_city(vehicle_instance):
    return vehicle_instance.city


def print_invoices(these_vehicles):
    invoices_printed = 0
    for vehicle in these_vehicles:
        if isinstance(vehicle, Car):
            vehicle_type = 'Car'
        elif isinstance(vehicle, Truck):
            vehicle_type = 'Truck'
        elif isinstance(vehicle, Motorcycle):
            vehicle_type = 'Motorcycle'
        else:
            raise ValueError(f'Expected Car, Truck or Motorcycle. This is a {type(vehicle)}.')

        print(f'\n\n\n\n{vehicle_type.upper()} REGISTRATION INVOICE')
        print(f'\nAMOUNT DUE: \t{vehicle.determine_annual_registration_fee():.2f}')
        print(f'\n{vehicle.first_name} {vehicle.last_name}')
        print(vehicle.street_address_1)
        if vehicle.street_address_2:
            print(vehicle.street_address_2)
        print(f'{vehicle.city}, {vehicle.state}  {vehicle.zipcode}')
        print(f'\nMake:\t\t{vehicle.make}')
        print(f'Model:\t\t{vehicle.model}')
        print(f'Year:\t\t{vehicle.year}')
        print(f'Color:\t\t{vehicle.color}')
        print(f'VIN:\t\t{vehicle.vehicle_id}')
        if vehicle_type == 'Car':
            print(f'Fuel:\t\t{vehicle.fuel_type}')
        elif vehicle_type == 'Truck':
            print(f'Gross WT:\t{vehicle.gross_weight:,}')
        elif vehicle_type == 'Motorcycle':
            print(f'Displacement in ccs:\t{vehicle.displacement_in_ccs:,}')
        else:
            raise ValueError(f'Expected Car or Truck. This is {vehicle_type}.')
        invoices_printed += 1

    print(f'\n\n\n\n\n{invoices_printed} invoices have been printed.')


main()
