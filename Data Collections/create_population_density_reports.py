"""Print a report of country records from a file in two different sort orders."""

from my_countries import Country


def main():
    countries = get_countries()

    countries.sort(key=by_country_name)
    print_report(countries, 'BY COUNTRY NAME')

    countries.sort(key=by_calculate_population_density_per_square_mile, reverse=True)
    print_report(countries, 'BY DESCENDING POPULATION DENSITY PER SQUARE MILE')


def get_countries():
    data_directory_name = 'data'
    infile_name = input('Please enter the input filename: ')
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r', encoding='utf-8')
    my_countries = []
    for line in infile:
        country_name, population, area_in_square_miles = line.split(';')
        my_countries.append(
            Country(country_name, int(population), int(area_in_square_miles))
        )
    infile.close()
    return my_countries


def by_country_name(country_instance):
    return country_instance.country_name


def by_calculate_population_density_per_square_mile(country_instance):
    return country_instance.calculate_population_density_per_square_mile()


def print_report(these_countries, report_title):
    print()
    print()
    print(f'{report_title:^80}')
    print()
    print(f'{"Country":<20}{"Population":>20}{"Area":>20}{"Density":>20}')
    print(f'{"":<20}{"":>20}{"(SQMI)":>20}{"(/SQMI)":>20}')
    for country in these_countries:
        print(f'{country.country_name:<20}'
              f'{country.population:>20,}'
              f'{country.area_in_square_miles:>20,}'
              f'{country.calculate_population_density_per_square_mile():>20,}')


main()