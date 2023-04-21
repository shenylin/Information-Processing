"""Author Python code to create a set of common passwords."""


def most_common_passwords():
    data_directory_name = 'data'
    infile_name = 'top_100_most_common_passwords.txt'
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r', encoding='utf-8')
    infile_to_list = infile.readlines()

    for i in range(len(infile_to_list)):
        common_passwords.append(infile_to_list[i].strip('\n'))

    print('COMMON_PASSWORDS = {')
    for line in infile:
        password = line.strip()
        common_password_count += 1
        print(f"                   '{password}',")

    print('                   }')

    infile.close()
    print(f'{common_password_count} common passwords were added to the set literal.')


main()
