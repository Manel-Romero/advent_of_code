# https://adventofcode.com/2025/day/7
# Laboratories

# Part 1
with open(r'c:\CP_UPV\advent_of_code\day7\day7.input', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()
    lines = [list(l) for l in lines]

source = lines[0].index('S')
lines[1][source] = '|'
counter = 0
for l in range(1, len(lines) - 1):
    for c in range(len(lines[l])):
        if lines[l-1][c] == '|':
            if lines[l][c] == '.':
                lines[l][c] = '|'
            elif lines[l][c] == '^':
                lines[l][c+1] = '|'
                lines[l][c-1] = '|'
                counter += 1
print(counter)


# Part 2
with open(r'c:\CP_UPV\advent_of_code\day7\day7.input', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()
    lines = [list(l) for l in lines]

source = lines[0].index('S')
w = len(lines[0])
h = len(lines)
counts = [0] * w
counts[source] = 1
for r in range(1, h):
    next_counts = [0] * w
    for c in range(w):
        v = counts[c]
        if v:
            if lines[r][c] == '.':
                next_counts[c] += v
            elif lines[r][c] == '^':
                next_counts[c - 1] += v
                next_counts[c + 1] += v
    counts = next_counts
print(sum(counts))
