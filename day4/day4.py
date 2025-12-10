# https://adventofcode.com/2025/day/4
# Printing Department

# Part 1
with open(r'c:\CP_UPV\advent_of_code\day4\day4.input', 'r', encoding='utf-8') as f:
    lines = [x for x in f.read().split()]
sol = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '@':
            adjacent = 0
            if i > 0:
                if lines[i-1][j] == '@':
                    adjacent += 1
            if i < len(lines)-1:
                if lines[i+1][j] == '@':
                    adjacent += 1
            if j > 0:
                if lines[i][j-1] == '@':
                    adjacent += 1
            if j < len(lines[i])-1:
                if lines[i][j+1] == '@':
                    adjacent += 1
            if j > 0 and i > 0:
                if lines[i-1][j-1] == '@':
                    adjacent += 1
            if j < len(lines[i])-1 and i > 0:
                if lines[i-1][j+1] == '@':
                    adjacent += 1
            if j > 0 and i < len(lines)-1:
                if lines[i+1][j-1] == '@':
                    adjacent += 1
            if j < len(lines[i])-1 and i < len(lines)-1:
                if lines[i+1][j+1] == '@':
                    adjacent += 1
            if adjacent < 4:
                sol += 1
print(sol)


# Part 2
with open(r'c:\CP_UPV\advent_of_code\day4\day4.input', 'r', encoding='utf-8') as f:
    lines = [x for x in f.read().split()]

sol = 0
can_take = True
while can_take:
    can_take = False
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '@':
                adjacent = 0
                if i > 0:
                    if lines[i-1][j] == '@':
                        adjacent += 1
                if i < len(lines)-1:
                    if lines[i+1][j] == '@':
                        adjacent += 1
                if j > 0:
                    if lines[i][j-1] == '@':
                        adjacent += 1
                if j < len(lines[i])-1:
                    if lines[i][j+1] == '@':
                        adjacent += 1
                if j > 0 and i > 0:
                    if lines[i-1][j-1] == '@':
                        adjacent += 1
                if j < len(lines[i])-1 and i > 0:
                    if lines[i-1][j+1] == '@':
                        adjacent += 1
                if j > 0 and i < len(lines)-1:
                    if lines[i+1][j-1] == '@':
                        adjacent += 1
                if j < len(lines[i])-1 and i < len(lines)-1:
                    if lines[i+1][j+1] == '@':
                        adjacent += 1
                if adjacent < 4:
                    sol += 1
                    lines[i] = lines[i][:j] + 'x' + lines[i][j+1:]
                    can_take = True
print(sol)

