# https://adventofcode.com/2025/day/5
# Cafeteria

# Part 1
with open(r'c:\CP_UPV\advent_of_code\day5\day5rang.input', 'r', encoding='utf-8') as f:
    ranges = [x for x in f.read().split()]
    ranges = [x.split("-") for x in ranges]
    ranges = [[int(x) for x in y] for y in ranges]

with open(r'c:\CP_UPV\advent_of_code\day5\day5num.input', 'r', encoding='utf-8') as f:
    nums = [x for x in f.read().split()]
    nums = [int(x) for x in nums]

sol = 0

for num in nums:
    for rangen in ranges:
        num1 = int(rangen[0])
        num2 = int(rangen[1])
        if num1 <= num <= num2:
            sol += 1
            break
print(sol)


# Part 2
with open(r'c:\CP_UPV\advent_of_code\day5\day5rang.input', 'r', encoding='utf-8') as f:
    ranges = [x for x in f.read().split()]
    ranges = [x.split("-") for x in ranges]
    ranges = [[int(x) for x in y] for y in ranges]

ranges_tuples = [(int(a), int(b)) for a, b in ranges]
ranges_tuples.sort()

sol = 0

merged = []
for i, f in ranges_tuples:
    if not merged or i > merged[-1][1] + 1:
        merged.append([i, f])
    else:
        if f > merged[-1][1]:
            merged[-1][1] = f
sol = sum(f - i + 1 for i, f in merged)
print(sol)
