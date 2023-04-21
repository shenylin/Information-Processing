"""Examine each word in a line user input to count numeric characters."""


def main():
    numbers = '0123456789'
    line = input('Please enter a line of text to be analyzed: ')
    words = line.split()

    print()
    for word in words:
        numeric_character_count = 0
        for character in numbers:
            numeric_character_count += word.count(character)
        print(f'"{word}" contains {numeric_character_count} numeric characters.')

    print(f'\n{len(words)} words were analyzed.')


main()