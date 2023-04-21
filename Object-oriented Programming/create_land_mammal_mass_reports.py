"""print a report of land mammal mass records from a file in two different sort orders."""

from my_land_mammals import LandMammal


def main():
    land_mammals = get_land_mammals()

    land_mammals.sort(key=by_LandMammal_name)
    print_report(land_mammals, 'BY LAND MAMMAL NAME')

    land_mammals.sort(key=by_range_of_mass, reverse=True)
    print_report(land_mammals, 'BY DESCENDING RANGE OF MASS IN POUNDS')


def get_land_mammals():
    data_directory_name = 'data'
    infile_name = input('Please enter the input filename: ')
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r', encoding='utf-8')
    my_land_mammals = []
    for line in infile:
        LandMammal_name, minimal_mass_as_string, maximum_max_as_string = line.split(',')
        my_land_mammals.append(
            LandMammal(LandMammal_name, int(minimal_mass_as_string), int(maximum_max_as_string))
        )
    infile.close()
    return my_land_mammals


def by_LandMammal_name(land_mammal_instance):
    return land_mammal_instance.LandMammal_name


def by_range_of_mass(land_mammal_instance):
    return land_mammal_instance.calculate_range_of_mass_in_pounds()


def print_report(these_land_mammals, report_title):
    print()
    print()
    print(f'{report_title:^60}')
    print()
    print(f'{"Land Mammal":<20}{"Minimum Mass":>15}{"Maximum Mass":>15}{"Range of Mass":>15}')
    print(f'{"Name":<20}{"in Pounds":>15}{"in Pounds":>15}{"in Pounds":>15}')
    for land_mammal in these_land_mammals:
        print(f'{land_mammal.LandMammal_name:<20}'
              f'{land_mammal.minimum_mass_in_pounds:>15,}'
              f'{land_mammal.maximum_mass_in_pounds:>15,}'
              f'{land_mammal.calculate_range_of_mass_in_pounds():>15,}')


main()



