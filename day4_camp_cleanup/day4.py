from typing import Set

with open("day4_camp_cleanup/input.txt") as f:
    lines = f.read().splitlines()

parsed_lines = [e.split(',') for e in lines]

def parse_range(section_numbers:str) -> Set[int]:
    n1, n2 = section_numbers.split('-')
    return set(range(int(n1), int(n2) + 1))

res = 0
for pairs in parsed_lines:
    elf1, elf2 = pairs
    seats_elf1 = parse_range(elf1)
    seats_elf2 = parse_range(elf2)
    if seats_elf1.issubset(seats_elf2) or seats_elf2.issubset(seats_elf1):
        res += 1

print(res)

