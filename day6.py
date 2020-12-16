# Part 1
with open('Advent of Code/input_day_6.txt', 'r+') as file:
    data = file.readlines()
    joined_data = "".join(data)
    one_group_multiple_lines = joined_data.split("\n\n")
    one_group_per_line = [line.replace("\n", "") for line in one_group_multiple_lines]
    number_of_yes_per_group = [len(set(line)) for line in one_group_per_line]
    total = sum(number_of_yes_per_group)

# Part 2
with open('Advent of Code/input_day_6.txt', 'r+') as file:
    data = file.readlines()
    joined_data = "".join(data)
    one_group_multiple_lines = joined_data.split("\n\n")
    answers_per_group = [line.replace("\n", " ").split(" ") for line in one_group_multiple_lines]
    for group in answers_per_group:
        for i in range(len(group)):
            group[i] = {char for char in group[i]}
        group[0] = group[0].intersection(*group)
        del group[1:]
    all_yes_per_group = [len(result) for group in answers_per_group for result in group]
    total = sum(all_yes_per_group)
