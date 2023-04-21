"""Using a dictionary, lookup distribute race ribbons on a series of place numbers supplied by the user."""


def main():
    distribute_race_ribbon_dictionary = create_ribbon_dictionary()
    entry_as_string = input('Please enter place finished (1, 2, 3...): ')

    while entry_as_string != '':
        try:
            place_number = int(entry_as_string)
            ribbon_color = determine_ribbon_color(place_number, distribute_race_ribbon_dictionary)
            print(f'Ribbon Awarded: {ribbon_color}\n')
        except ValueError:
            print(f'A integer value was expected. You entered {entry_as_string}')
        entry_as_string = input('Please enter place finished (1, 2, 3...): ')
    print('\nThanks for playing.')

def create_ribbon_dictionary():
    ribbon_color = {
        1: 'Blue',
        2: 'Red',
        3: 'Orange',
        4: 'Gold',
        5: 'Green',
        6: 'Purple'
    }
    return ribbon_color

def determine_ribbon_color(place_number, distribute_race_ribbon_dictionary):
    if place_number < 1:
        ribbon_color = 'ERROR - Place must be greater than zero.'
    else:
        ribbon_color = distribute_race_ribbon_dictionary.get(place_number, f'White')
    return ribbon_color


main()
