import string
with open ('day3_rucksack/input.txt') as f:
    lines = f.read().splitlines()

parsed_lines = [(line[:int(len(line) / 2)], line[int(len(line) / 2):]) for line in lines]

#part 1
def calculate_priority(letter):
    if letter.isupper():
        return string.ascii_lowercase.index(letter.lower()) + 27
    return string.ascii_lowercase.index(letter) + 1

priority = 0
for line in parsed_lines:
    compartment1, compartment2 = line
    overlapping_item = set(compartment1).intersection(set(compartment2)).pop()
    priority += calculate_priority(overlapping_item)

print(priority)

#part 2
group_prio = 0
grouped_elves = [lines[n:n+3] for n in range(0, len(lines), 3)]
for line in grouped_elves:
    elf1, elf2, elf3 = line
    overlapping_item = set.intersection(set(elf1), set(elf2), set(elf3)).pop()
    group_prio += calculate_priority(overlapping_item)

print(group_prio)