# Part 1
with open('Advent of Code/input_day_4.txt', 'r+') as file:
    batch = file.readlines()
    joined_batch = "".join(batch)
    batch = joined_batch.split("\n\n")
    records = [record.replace("\n", " ").split(" ") for record in batch]
    nr_valid_passwords = 0
    for record in records:
        if len(record) == 8:
            nr_valid_passwords = nr_valid_passwords + 1
        elif len(record) == 7 and not any("cid" in rec for rec in record):
            nr_valid_passwords = nr_valid_passwords + 1
    print(nr_valid_passwords)

import pandas as pd
import numpy as np
# Part 2
with open('Advent of Code/input_day_4.txt', 'r+') as file:
    batch = file.readlines()
    joined_batch = "".join(batch)
    batch = joined_batch.split("\n\n")
    records = [record.replace("\n", " ").split(" ") for record in batch]
    records_dict = {}
    for index, record in enumerate(records):
        records_dict[index] = {field.split(":")[0]: field.split(":")[1] for field in record}
    data = pd.DataFrame(records_dict).T

    data['byr'] = data['byr'].apply(lambda field: field if 1920 <= float(field) <= 2002 else np.nan)
    data['iyr'] = data['iyr'].apply(lambda field: field if 2010 <= float(field) <= 2020 else np.nan)
    data['eyr'] = data['eyr'].apply(lambda field: field if 2020 <= float(field) <= 2030 else np.nan)
    data['unit'] = data['hgt'].apply(lambda field: str(field)[-2:])
    data['hgt'] = data['hgt'].apply(lambda field: str(field)[:-2] if type(field) != float else field)
    data['hgt'] = data.apply(lambda row: row['hgt'] if row['hgt'] != '' and ((150 <= float(row['hgt']) <= 193 and row['unit'] == 'cm') or (59 <= float(row['hgt']) <= 76 and row['unit'] == 'in')) else np.nan, axis=1)
    data['hcl'] = data['hcl'].apply(lambda field: field if type(field) != float and field[0] == "#" and len(field) == 7 else np.nan)
    valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    data['ecl'] = data['ecl'].apply(lambda field: field if field in valid_eye_colors else np.nan)
    data['pid'] = data['pid'].apply(lambda field: field if len(str(field)) == 9 and str(field).isnumeric() == True else np.nan)
    data['cid'] = data['cid'].fillna(0)

    valid_passports = data.dropna()
