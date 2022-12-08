with open('5inp.txt') as f:
    lines = f.readlines()

positions = {
    1: ["D", "L", "V", "T", "M", "H", "F"],
    2: ["H", "Q", "G", "J", "C", "T", "N", "P"],
    3: ["R", "S", "D", "M", "P", "H"],
    4: ["L", "B", "V", "F"],
    5: ["N", "H", "G", "L", "Q"],
    6: ["W", "B", "D", "G", "R", "M", "P"],
    7: ["G", "M", "N", "R", "C", "H", "L", "Q"],
    8: ["C", "L", "W"],
    9: ["R", "D", "L", "Q", "J", "Z", "M", "T"]
}


for idx, line in enumerate(lines[10:]):
    chars = line.split(" ")
    move = int(chars[1])
    start_stack = int(chars[3])
    end_stack = int(chars[-1])

    for i in range(move):
        mover = positions[start_stack][-1]
        positions[start_stack].pop()
        positions[end_stack].append(mover)

print(positions)
s = ""
for k,v in positions.items():
    s += v[-1]
    # mover = 
print(f"Part One: {s}")

# Part Two
positions = {
    1: ["D", "L", "V", "T", "M", "H", "F"],
    2: ["H", "Q", "G", "J", "C", "T", "N", "P"],
    3: ["R", "S", "D", "M", "P", "H"],
    4: ["L", "B", "V", "F"],
    5: ["N", "H", "G", "L", "Q"],
    6: ["W", "B", "D", "G", "R", "M", "P"],
    7: ["G", "M", "N", "R", "C", "H", "L", "Q"],
    8: ["C", "L", "W"],
    9: ["R", "D", "L", "Q", "J", "Z", "M", "T"]
}

for idx, line in enumerate(lines[10:]):
    chars = line.split(" ")
    move = int(chars[1])
    start_stack = int(chars[3])
    end_stack = int(chars[-1])

    movers = positions[start_stack][-move:]
    positions[end_stack] += movers
    positions[start_stack] = positions[start_stack][:-move]

s = ""

for k, v in positions.items():
    s += v[-1]
print(f"Part Two: {s}")