# Part 1
with open("/Users/axelwest/Desktop/input_day_1.txt", "r+") as file:
    numbers = file.readlines()
    list_of_numbers = [int(number) for number in numbers]
    for number_1 in list_of_numbers:
        for number_2 in list_of_numbers:
            if number_1 + number_2 == 2020:
                print(f'First number is {number_1}, second number is {number_2}')
                print(f'Their product is {number_1 * number_2}')


# Part 2                
with open("/Users/axelwest/Desktop/input_day_1.txt", "r+") as file:
    numbers = file.readlines()
    list_of_numbers = [int(number) for number in numbers]
    for number_1 in list_of_numbers:
        for number_2 in list_of_numbers:
            for number_3 in list_of_numbers:
                if number_1 + number_2 + number_3 == 2020:
                    print(f'First number is {number_1}, second number is {number_2}, third number is {number_3}')
                    print(f'Their product is {number_1 * number_2 * number_3}')