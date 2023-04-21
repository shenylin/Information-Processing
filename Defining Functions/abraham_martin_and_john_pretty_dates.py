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

        print(f'Born: {format_date_string(date_of_birth)}')
        print(f'Died: {format_date_string(date_of_death)}')


def format_date_string(date):

    date = datetime.strptime(date, "%Y-%m-%d")
    month = datetime.strptime(date, "%Y-%m-%d")





main()
