"""Demonstrate a simple lookup coded inline."""


def main():
    region_code = int(input('Please enter region code (1, 2, 3, 4): '))

    if region_code == 1:
        region_name = 'Northeast'
    elif region_code == 2:
        region_name = 'Southeast'
    elif region_code == 3:
        region_name = 'Northwest'
    elif region_code == 4:
        region_name = 'Southwest'
    else:
        region_name = 'Invalid Region'

    print(f'\nRegion code {region_code} is {region_name}.')


main()
