with open ('day1_calorie_counting/input.txt') as f:
    lines = f.read()

split_file = lines.split("\n\n")
elves = [elf.split('\n') for elf in split_file]
elves = [[int(e)for e in elf] for elf in elves]

descending_calories_list = sorted([sum(elf) for elf in elves], key=int, reverse=True)

print(sum(descending_calories_list[:3]))