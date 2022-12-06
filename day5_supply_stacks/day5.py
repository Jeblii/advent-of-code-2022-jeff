from collections import defaultdict
import re

with open("day5_supply_stacks/input.txt") as f:
    lines = f.read()

crates, instructions = lines.split("\n\n")
instructions = instructions.split("\n")
crate_lines = defaultdict(list)

for line in crates.splitlines():
    if not any([el.isalpha() for el in line]):
        continue
    else:
        layer = [line[i + 1 : i + 2] for i in range(0, len(line), 4)]
        for i, contents in enumerate(layer):
            if contents.isalpha():
                if not (i + 1) in crate_lines.keys():
                    crate_lines[(i + 1)] = [contents]
                else:
                    crate_lines[(i + 1)].append(contents)

# part one
def move(n: int, from_tower: int, to_tower: int):
    for i, crate in enumerate(crate_lines[from_tower][:n]):
        crate_lines[to_tower].insert(0, crate)

    for i in range(n):
        crate_lines[from_tower].pop(0)
    return


for instruction in instructions:
    amount, start, finish = re.findall(r"\b\d+\b", instruction)
    move(int(amount), int(start), int(finish))

message = "".join([v[0] for k, v in sorted(crate_lines.items())])
print(message)

# part two
def move_two(n: int, from_tower: int, to_tower: int):
    for i, crate in enumerate(crate_lines[from_tower][:n]):
        crate_lines[to_tower].insert(i, crate)
        crate_lines[from_tower].pop(0)
    print(sorted(crate_lines.items()))

    # for i in range(n):

    return


print(sorted(crate_lines.items()))

for instruction in instructions:
    amount, start, finish = re.findall(r"\b\d+\b", instruction)
    move_two(int(amount), int(start), int(finish))

message = "".join([v[0] for k, v in sorted(crate_lines.items())])
print(message)
