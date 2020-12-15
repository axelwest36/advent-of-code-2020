import math 

def get_row(code):
    min_row = 0
    max_row = 127
    while len(code) > 4:
        if code[0] == "F":
            max_row = math.floor((max_row+min_row)/2)
            code = code[1:]
        elif code[0] == "B":
            min_row = round((max_row+min_row)/2)
            code = code[1:]
    if code[0] == "B":
        row = max_row
    elif code[0] == "F":
        row = min_row
    return row

def get_column(code):
    code = code[-3:]
    max_col = 7
    min_col = 0
    while len(code) > 1:
        if code[0] == "L":
            max_col = math.floor((max_col+min_col)/2)
            code = code[1:]
        elif code[0] == "R":
            min_col = round((max_col+min_col)/2)
            code = code[1:]
    if code[0] == "L":
        col = min_col
    elif code[0] == "R":
        col = max_col
    return col

def get_seat_id(code):
    row = get_row(code)
    col = get_column(code)
    seat_id = row * 8 + col
    return seat_id

# Part 1
with open('Advent of Code/input_day_5.txt', 'r+') as file:
    seat_ids = [get_seat_id(f.strip("\n")) for f in file]
    len(seat_ids) == len(set(seat_ids)) # Sanity check to see if all seat ids are unique
    max(seat_ids)
    
# Part 2
with open('Advent of Code/input_day_5.txt', 'r+') as file:
    seat_ids = [get_seat_id(f.strip("\n")) for f in file]
    sorted_seat_ids = seat_ids.sort()
    missing_seat_ids = [sorted_seat_ids[i]+1 for i in range(len(sorted_seat_ids)-1) if sorted_seat_ids[i+1] != sorted_seat_ids[i]+1]