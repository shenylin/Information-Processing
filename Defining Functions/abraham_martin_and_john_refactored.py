"""
This program  prints the name, date of birth, and date of death of the four key figures
mentioned in the song "Abraham, Martin and John" by Dick Holler:

    Abraham Lincoln
    Martin Luther King Jr.
    John F. Kennedy
    Robert F. Kennedy
"""
# source: https://en.wikipedia.org/wiki/Abraham,_Martin_and_John


def main():
    key_figure_facts = [
        ('Abraham Lincoln', '02121809', '04151865'),
        ('Martin Luther King Jr.', '01151929', '04041968'),
        ('John F. Kennedy', '05291917', '11221963'),
        ('Robert F. Kennedy', '11201925', '06061968')
    ]

    print('Key Figures from the Song "Abraham, Martin and John" by Dick Holler:')
    for fact_tuple in key_figure_facts:
        name, date_of_birth, date_of_death = fact_tuple
        print()
        print(name)
        print(f'Born: {date_formats_string(date_of_birth)},"/"')
        print(f'Died: {date_of_death[0:2]}/{date_of_death[2:4]}/{date_of_death[4:8]}')

def date_formats_string(date_of, seperator):
    return f'{date_of[5:7]}{seperator}{date_of[8:10]}{seperator}{date_of[0:4]}'


main()
