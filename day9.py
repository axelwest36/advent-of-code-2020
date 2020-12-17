# Part 1
def check_validity(current_num, data, preamble=25):
    if (data.index(current_num) - preamble) >= 0:
        for num1 in data[(data.index(current_num) - preamble):data.index(current_num)]:
            for num2 in data[(data.index(current_num) - preamble):data.index(current_num)]:
                if int(num1) + int(num2) == int(current_num):
                    return True
                else:
                    continue
        return False
    else:
        return True

with open('Advent of Code/input_day_9.txt', 'r+') as file:
    data = file.readlines()
    lines = [f.strip('\n') for f in data]
    bool_list = [check_validity(line, lines, preamble=25) for line in lines]
    false_indices = bool_list.index(False)
    print(false_indices+1, lines[false_indices])