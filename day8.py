# Part 1
def read_instructions(instructions):
    lines_read = []
    accumulator = 0
    current_line = 0
    while current_line not in lines_read:
        if instructions[current_line][0] == "acc":
            accumulator += int(instructions[current_line][1])
            lines_read.append(current_line)
            current_line += 1
        elif instructions[current_line][0] == "jmp":
            lines_read.append(current_line)
            current_line += int(instructions[current_line][1])
        elif instructions[current_line][0] == "nop":
            lines_read.append(current_line)
            current_line += 1
    return accumulator

with open("Advent of Code/input_day_8.txt", "r+") as file:
    instructions = [f.strip("\n").split(" ") for f in file]
    result = read_instructions(instructions)
    print(result)

# Part 2
def swap_line(base_instructions, current_line):
    instructions = base_instructions
    if instructions[current_line][0] == "jmp":
        instructions[current_line][0] = "nop"
    elif instructions[current_line][0] == "nop":
        instructions[current_line][0] = "jmp"
    return instructions

def fix_instructions(instructions):
    lines_read = []
    accumulator = 0
    current_line = 0
    while current_line < len(instructions):
        if current_line in lines_read:
            new_instructions = swap_line(instructions, current_line)
            fix_instructions(new_instructions)
        if instructions[current_line][0] == "acc":
            accumulator += int(instructions[current_line][1])
            lines_read.append(current_line)
            current_line += 1
        elif instructions[current_line][0] == "jmp":
            lines_read.append(current_line)
            current_line += int(instructions[current_line][1])
        elif instructions[current_line][0] == "nop":
            lines_read.append(current_line)
            current_line += 1
    return accumulator

with open("Advent of Code/input_day_8.txt", "r+") as file:
    instructions = [f.strip("\n").split(" ") for f in file]
    result = fix_instructions(instructions)
    print(result)
