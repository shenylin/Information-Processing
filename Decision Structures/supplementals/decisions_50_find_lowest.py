"""Demonstrate general approach to finding the lowest value in a sequence."""


def main():
    input_list = [1, 5, 99, -1, 0, 23, 55, 96, -2048, 4096, -99]
    # input_list = []

    if len(input_list) == 0:
        print('The input list is empty.')
    else:
        lowest_entry_so_far = input_list[0]

        for entry in input_list:
            if entry < lowest_entry_so_far:
                lowest_entry_so_far = entry

        print(f'There are {len(input_list)} entries in the input list.')
        print(f'The lowest value is {lowest_entry_so_far}.')


main()
