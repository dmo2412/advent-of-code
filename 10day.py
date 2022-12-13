# # addx V takes 2 cycles to complete. After 2 cycles the X register is increased by the value of V.
# # noop takes on cycle to complete and has no other effect.

with open('10inp.txt') as f:
    lines = f.readlines()

x = 1
cycle = 0
previous_num = 0
total_x = 0
hit_cycle = 20
final_x = 0


for idx, line in enumerate(lines):
    line = line.strip("\n")
    line = line.split(" ")
    if len(line) == 2:
        line[1] = int(line[1])
        for count in range(2):
            cycle += 1
            if cycle == hit_cycle:
                hit_cycle += 40
                total_x += cycle * x 
                final_x += total_x
                total_x = 0
        x += line[1]
    else:
        cycle += 1
        if cycle == hit_cycle:
            total_x += cycle * x
            hit_cycle += 40
            final_x += total_x
            total_x = 0

print(f"Part One: {final_x}")

# Part Two 

# print(sprite)
curr_crt = ""
x = 1
successes = [-1, 0, 1]
ans = []

with open('10inp.txt') as f:
    lines = f.readlines()

row = 0
for idx, line in enumerate(lines):
    line = line.strip("\n")
    line = line.split(" ")
    
    if len(line) == 2:
        line[1] = int(line[1])
        for i in range(2):
            if len(curr_crt) == 40:
                ans.append(curr_crt)
                curr_crt = ""
            if len(curr_crt) - x in successes:
                curr_crt += "#"
            else:
                curr_crt += " "
        x += line[1]
    else:
        if len(curr_crt) == 40:
            ans.append(curr_crt)
            curr_crt = ""
        if len(curr_crt) - x in successes:
            curr_crt += "#"
        else:
            curr_crt += " "
ans.append(curr_crt)


for line in ans:
    print(line)

print(10%11)


                







