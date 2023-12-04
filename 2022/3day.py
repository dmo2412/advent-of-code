# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

import string 

letters = {}

for idx, i in enumerate(string.ascii_letters): 
    letters[i] = idx + 1
print(letters)
with open('3inp.txt') as f:
    lines = f.readlines()

total = 0

for idx, line in enumerate(lines):
    if idx == len(lines) -1:
        dist = (len(line)) // 2
        first = line[:dist]
        second = line[dist:]
    else:
        dist = (len(line) - 1) // 2
        first = line[:dist]
        second = line[dist:-1]
    t1 = {}
    t2 = {}
    for i in range(len(first)):
        if first[i] == second[i]:
            total += letters[first[i]]
            break
        elif first[i] in t2:
            total += letters[first[i]]
            break
        elif second[i] in t1:
            total += letters[second[i]]
            break
        else:
            t1[first[i]] = True
            t2[second[i]] = True

print(f"Part One: {total}")


# Part Two
count = 0
i = 0
while i < len(lines):
    for char in lines[i]:
        if char in lines[i+1] and char in lines[i+2]:
            count += letters[char]
            break
    i += 3
print(f"Part Two: {count}")