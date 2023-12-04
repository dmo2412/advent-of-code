with open('16inp.txt') as f:
    lines = f.readlines()

pressure = {}
directions = {}

for idx, line in enumerate(lines):
    line = line.strip("\n")
    eq_index = line.find("=")
    colon_index = line.find(";")
    rate = int(line[eq_index+1:colon_index])
    valve_idx = line.find("ve ")
    valve = line[valve_idx+3:valve_idx+5]
    valve_dir_idx = line.find("valve")
    dir_valves = line[valve_dir_idx+6:].split(", ")
    if len(dir_valves) > 1:
        dir_valves[0] = dir_valves[0][1:]
    directions[valve] = dir_valves
    pressure[valve] = rate

start = "AA"
minutes = 30
total_pressure = 0
open_valves = []

# for valve, dir in directions.items():
while minutes > 0:
    valves = directions[start]
    highest = -1
    for valve in valves:
        if pressure[valve] > highest and valve not in open_valves:
            highest = pressure[valve]
            start = valve
    if highest > 0:
        open_valves.append(start)
        total_pressure += highest * minutes
        minutes -= 2
    else:
        minutes -= 1
    print(start)
print(total_pressure) 
    
    
    