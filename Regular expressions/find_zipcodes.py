"""
Extract matches to 4 different zipcode patterns from input file.

Matched patterns include:
    99999
    99999-9999
"""

import re


def main():
    print('Extract matches to 2 different zipcode patterns from input file.')
    data_directory_name = 'data'
    infile_name = input('Please enter the input filename: ')
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r', encoding='utf-8')
    zipcodes_found = []

    for line in infile:
        zipcodes = re.findall(r'\d{5}-\d{4}|\d{5}', line)
        zipcodes_found.extend(zipcodes)

    infile.close()

    if not zipcodes_found:
        print('\nNo zipcodes were found in the input file.')
    else:
        print('\nThe following zipcodes were found in the input file:')
        for zipcode in zipcodes_found:
            print(f'  {zipcode}')


main()
