from gpa import Student


def main():
    mary = Student('Mary Q. Scholar', 100, 400)

    print(mary)
    print()
    print(mary.getName())
    print(mary.getHours())
    print(mary.getQPoints())
    print('Mary''s GPA is', mary.gpa())


main()
