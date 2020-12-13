# Part 1
with open("/Users/axelwest/Desktop/Advent of Code/input_day_2.txt", "r+") as file:
    passwords = file.readlines()
    list_of_passwords = [password.split(":") for password in passwords]
    character_occurrences = [password[1].count(f'{password[0][-1]}') for password in list_of_passwords]
    occurrences_criteria = [password[0].split("-") for password in list_of_passwords]
    number_valid_passwords = 0
    for i in range(len(character_occurrences)):
        if int(occurrences_criteria[i][0]) <= character_occurrences[i] <= int(occurrences_criteria[i][1][:-2]):
            number_valid_passwords = number_valid_passwords + 1
    print(f'Number of valid passwords is {number_valid_passwords}')

# Part 2
with open("/Users/axelwest/Desktop/Advent of Code/input_day_2.txt", "r+") as file:
    passwords = file.readlines()
    list_of_passwords = [password.split(":") for password in passwords]
    occurrences_criteria = [tuple(password[0].split("-")) for password in list_of_passwords]
    passwords = [password[1][1:] for password in list_of_passwords]
    positions = [(int(i), int(j[:-2])) for i, j in occurrences_criteria]
    letters = [j[1][-1] for j in occurrences_criteria]
    number_valid_passwords = 0
    for i in range(len(list_of_passwords)):
        if (passwords[i][positions[i][0]-1] == letters[i]) ^ (passwords[i][positions[i][1]-1] == letters[i]):
            number_valid_passwords = number_valid_passwords + 1
    print(f'Number of valid passwords is {number_valid_passwords}')