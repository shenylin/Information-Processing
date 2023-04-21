"""Print the song 99 Bottles of Beer as adapted for a programming exercise."""


def main():
    write_title()

    num_bottles = 99
    while num_bottles > 0:
        print(str(num_bottles) + " bottles of beer on the wall,", str(num_bottles) + " bottles of beer.")
        print("Take one down and pass it around,", str(num_bottles - 1) + " bottles of beer on the wall.")
        print()
        num_bottles = num_bottles - 1

    no_more_bottle()


def write_title():
    print('99 Bottles of Beer')
    print('Traditional')
    print()


def no_more_bottle():
    print('No more bottles of beer on the wall, no more bottles of beer.')
    print('Go to the store and buy some more, 99 bottles of beer on the wall.')


main()


