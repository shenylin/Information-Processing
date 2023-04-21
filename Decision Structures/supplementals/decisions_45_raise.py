"""
Demonstrate raising an exception in called code.
Demonstrate catching an exception raised in called code and handling it.
"""


def main():
    try:
        region_code = int(input('Please enter region code (1, 2, 3, 4): '))
        region_name = lookup_region_name(region_code)
        print(f'\nRegion code {region_code} is {region_name}.')
    except ValueError as ve:
        print(f'\n{ve}')

    print('Thanks for playing.')


def lookup_region_name(region_code):
    if region_code == 1:
        region_name = 'Northeast'
    elif region_code == 2:
        region_name = 'Southeast'
    elif region_code == 3:
        region_name = 'Northwest'
    elif region_code == 4:
        region_name = 'Southwest'
    else:
        raise ValueError(f'Region code must be 1, 2, 3, or 4. This value is {region_code}.')
    return region_name


main()
