"""print a report of state/area records from a file in two different sort orders."""

from my_states import State


def main():
    states = get_states()

    states.sort(key=by_state_name)
    print_report(states, 'BY STATE NAME')

    states.sort(key=by_total_area, reverse=True)
    print_report(states, 'BY DESCENDING TOTAL AREA IN SQUARE MILES')


def get_states():
    data_directory_name = 'data'
    infile_name = input('Please enter the input filename: ')
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r', encoding='utf-8')
    my_states = []
    for line in infile:
        state_name, land_area_as_string, water_area_as_string = line.split(';')
        my_states.append(
            State(state_name, float(land_area_as_string), float(water_area_as_string))
        )
    infile.close()
    return my_states


def by_state_name(state_instance):
    return state_instance.state_name


def by_total_area(state_instance):
    return state_instance.calculate_total_area_in_square_miles()


def print_report(these_states, report_title):
    print()
    print()
    print(f'{report_title:^60}')
    print()
    print(f'{"State":<15}{"Land Area":>15}{"Water Area":>15}{"Total Area":>15}')
    print(f'{"":<15}{"(SQMI)":>15}{"(SQMI)":>15}{"(SQMI)":>15}')
    for state in these_states:
        print(f'{state.state_name:<15}'
              f'{state.land_area_in_square_miles:>15,.2f}'
              f'{state.water_area_in_square_miles:>15,.2f}'
              f'{state.calculate_total_area_in_square_miles():>15,.2f}')


main()
