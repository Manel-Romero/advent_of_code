# https://adventofcode.com/2025/day/1
# Secret Entrance

# Part 1
with open(r'c:\CP_UPV\advent_of_code\day1\day1.input', 'r', encoding='utf-8') as f:
    instructions = [x for x in f.read().split()]

combination = 50
sol = 0
for inst in instructions:
    if "R" in inst:
        combination += int(inst.replace("R", ""))
    else:
        combination -= int(inst.replace("L", ""))
    combination %= 100

    if combination == 0:
        sol += 1
print(sol)


# Part 2
with open(r'c:\CP_UPV\advent_of_code\day1\day1.input', 'r', encoding='utf-8') as f:
    instructions = [x for x in f.read().split()]

combination = 50
sol = 0
for inst in instructions:
    for i in range(int(inst.replace("R", "").replace("L", ""))):
        if "R" in inst:
            combination += 1
        else:
            combination -= 1
        combination %= 100

        if combination == 0:
            sol += 1    
print(sol)