# https://adventofcode.com/2025/day/2
# Lobby

# Part 1
with open(r'c:\CP_UPV\advent_of_code\day2\day2.input', 'r', encoding='utf-8') as f:
    IDlist = [x for x in f.read().split(",")]

def analizar(num1, num2):
    count = 0
    for i in range(num1, num2+1):
        if str(i)[:int(len(str(i))/2)] == str(i)[int(len(str(i))/2):]:
            count += i
    return count

sol = 0
for ID in IDlist:
    id1 = int(ID.split("-")[0])
    id2 = int(ID.split("-")[1])
    sol += analizar(id1, id2) if analizar(id1, id2) else 0

print(sol)


# Part 2
with open(r'c:\CP_UPV\advent_of_code\day2\day2.input', 'r', encoding='utf-8') as f:
    IDlist = [x for x in f.read().split(",")]

def analizar(num1, num2):
    count = 0
    for i in range(num1, num2 + 1):
        s = str(i)
        L = len(s)
        for k in range(1, L):
            if L % k != 0:
                continue
            patron = s[:k]
            if patron * (L // k) == s:
                count += i
                break
    return count

sol = 0
for ID in IDlist:
    id1, id2 = map(int, ID.split("-"))
    sol += analizar(id1, id2)

print(sol)