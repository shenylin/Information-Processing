"""Count color names in the slot machine file ignoring duplicate values on the same line"""


def main():
    data_directory_name = 'data'
    infile_name = input('Please enter the input filename: ')
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r', encoding='utf-8')
    color_count = {}

    for line in infile:
        slot_values = line.split()
        list_without_duplicates = new_list_without_duplicates(slot_values)
        for slot_value in list_without_duplicates:
            color_count[slot_value] = color_count.get(slot_value, 0) + 1

    infile.close()

    these_keys = list(color_count.keys())
    these_keys.sort()

    print()
    print(f'{"COLOR":<10}{"COUNT":>7}')
    for this_key in these_keys:
        print(f'{this_key:<10} {color_count.get(this_key):>7,}')


def new_list_without_duplicates(slot_values):
    return list(set(slot_values))


main()