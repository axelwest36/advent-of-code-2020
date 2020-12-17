# Part 1
with open("Advent of Code/input_day_10.txt", 'r+') as file:
    jolts = sorted([int(f.strip("\n")) for f in file])
    adapters_used = []
    diff_1 = []
    diff_3 = []
    for jolt1 in jolts:
        for jolt2 in jolts:
            if abs(jolt1 - jolt2) == 1 and jolt1 not in adapters_used and jolt2 not in adapters_used:
                diff_1.append((jolt1, jolt2))
                adapters_used.append(jolt1)
                adapters_used.append(jolt2)
            if abs(jolt1 - jolt2) == 3 and jolt1 not in adapters_used and jolt2 not in adapters_used:
                diff_3.append((jolt1, jolt2))
                adapters_used.append(jolt1)
                adapters_used.append(jolt2)
    print(len(diff_1) * len(diff_3))