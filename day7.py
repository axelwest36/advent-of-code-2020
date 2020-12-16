from parse import parse

def get_container_bags(rules, bag):
    for key, value in rules.items():
        if any(bag in val for val in value):
            list_of_container_bags.append(key)
            get_container_bags(rules, key)

def get_contained_bags(rules, start_bag, multiplier):
    bags = rules[start_bag]
    for bag in bags:
        if bag != "no other bags":
            parsed_bag = parse("{} {} {} {}", bag)
            if parsed_bag[1] + " " + parsed_bag[2] in dict_of_contained_bags.keys():
                dict_of_contained_bags[parsed_bag[1] + " " + parsed_bag[2]] += (int(parsed_bag[0]) * multiplier)
            else:
                dict_of_contained_bags[parsed_bag[1] + " " + parsed_bag[2]] = (int(parsed_bag[0]) * multiplier)
            get_contained_bags(rules, parsed_bag[1] + " " + parsed_bag[2], int(parsed_bag[0])*multiplier)
        else:
            continue

# Part 1
with open("Advent of Code/input_day_7.txt", "r+") as file:
    rules = file.readlines()
    rules = {parse("{} bags contain {}.", rule)[0]: parse("{} bags contain {}.", rule)[1].split(", ")  for rule in rules}
    list_of_container_bags = []
    get_container_bags(rules, "shiny gold")
    print(len(set(list_of_container_bags)))

# Part 2
with open("Advent of Code/input_day_7.txt", "r+") as file:
    rules = file.readlines()
    rules = {parse("{} bags contain {}.", rule)[0]: parse("{} bags contain {}.", rule)[1].split(", ")  for rule in rules}
    dict_of_contained_bags = {}
    get_contained_bags(rules, 'shiny gold', 1)
    print(sum(dict_of_contained_bags.values()))