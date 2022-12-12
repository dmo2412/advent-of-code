import json
with open('9inp.txt') as f:
    lines = f.readlines()

tail_positions = {}
moves = {
    "U": 1,
    "D": -1,
    "L": -1,
    "R": 1
}
head_x = 0
head_y = 0
tail_x = 0
tail_y = 0



for idx, line in enumerate(lines):
    line = line.strip("\n")
    direction = line[0]
    if len(line) == 4:
        num_moves = int(line[-2:])
    else:
        num_moves = int(line[-1])
    
    if direction in ["U", "D"]:
        head_y += num_moves * moves[direction]
    elif direction in ["L", "R"]:
        head_x += num_moves * moves[direction]
    else:
        print("Youre bad at this")
    count = 0
    if abs(head_x - tail_x) > 1:
        while abs(head_x - tail_x) > 1:
            key = f"{tail_x},{tail_y}"
            tail_positions[key] = "X"
            tail_x += moves[direction]
            if tail_y != head_y:
                tail_y = head_y    
    if abs(head_y - tail_y) > 1:
        while abs(head_y - tail_y) > 1:
            key = f"{tail_x},{tail_y}"
            tail_positions[key] = "X"
            tail_y += moves[direction]
            if tail_x != head_x:
                tail_x = head_x
        
key = f"{tail_x},{tail_y}"
tail_positions[key] = "X"
print(f"Part One: {len(tail_positions)}")


# Part Two
moves = {
    "U": 1,
    "D": -1,
    "L": -1,
    "R": 1
}

def handle_next(start_x, start_y, next_x, next_y, index, direction, num_moves):   
    count = 0
    x_distance = abs(start_x - next_x)
    if x_distance > 1 and direction in ["L", "R"]:
        # print(next_x)
        # print(start_x)
        # print(index, num_moves)
        
        # y = f"{next_x, next_y}"
        while abs(start_x - next_x) > 1:
            # print(start_x)
            # print(next_x)
            # print("____________________")
            if index == 9:
                key = f"{next_x},{next_y}"
                tail_positions[key] = "X"
            # count += 1
            next_x += moves[direction]
            
            if next_y != start_y:
                next_y = start_y
    if abs(abs(start_y) - abs(next_y)) > 1 and direction in ["U", "D"]:
        # print(start_y, next_y, direction)
        count = 0
        while abs(start_y - next_y) > 1:
            if index == 9:
                key = f"{next_x},{next_y}"
                tail_positions[key] = "X"
            next_y += moves[direction]
            if next_x != start_x:
                next_x = start_x
    if index == 9:
        key = f"{next_x},{next_y}"
        tail_positions[key] = "X"
    return next_x, next_y               


head_x = 0
head_y = 0

x_positions = [0] * 10
y_positions = [0] * 10
tail_positions = {}
moves = {
    "U": 1,
    "D": -1,
    "L": -1,
    "R": 1
}

for line in lines:
    line = line.strip("\n")
    direction = line[0]
    if len(line) == 4:
        num_moves = int(line[-2:])
    else:
        num_moves = int(line[-1])

    if direction in ["U", "D"]:
        head_y += num_moves * moves[direction]
    elif direction in ["L", "R"]:
        head_x += num_moves * moves[direction]

    x_positions[0] = head_x
    y_positions[0] = head_y
    for i in range(1,10):
        # print(direction, num_moves)
        # print(x_positions[i-1], y_positions[i-1])
        # print(x_positions[i], y_positions[i])
        # print("________________________________")
        next_x, next_y = handle_next(x_positions[i-1], y_positions[i-1], x_positions[i], y_positions[i], i, direction, num_moves)
        x_positions[i] = next_x
        y_positions[i] = next_y
        # print(direction, num_moves)
        # print(x_positions[i-1], y_positions[i-1])
        # print(x_positions[i], y_positions[i])
        # print("________________________________")
        # print("________________________________")
        # print("________________________________")

print(len(tail_positions))

        
    
    


# two_x = 0
# two_y = 0
# three_x = 0
# three_y = 0
# four_x = 0
# four_y = 0
# five_x = 0
# five_y = 0
# six_x = 0
# six_y = 0
# seven_x = 0
# seven_y = 0
# eight_x = 0
# eight_y = 0
# nine_x = 0
# nine_y = 0
# tail_x = 0
# tail_y = 0


# Need to get 36