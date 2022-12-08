with open('6inp.txt') as f:
    lines = f.readlines()

line = lines[0]

i = 4
while i < len(line):
    chunk = line[i-4:i]
    chars = list(chunk)
    unique_chars = set(chars)
    if len(unique_chars) == 4:
        print(f"Part One: {i}")
        break
    i += 1


# Part Two 

line = lines[0]
i = 14

while i < len(line):
    chunk = line[i-14:i]
    chars = list(chunk)
    unique_chars = set(chars)
    if len(unique_chars) == 14:
        print(f"Part Two: {i}")
        break
    i += 1