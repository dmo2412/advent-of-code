# 12 red cubes
# 13 green cubes
# 14 blue cubes

with open('2inp.txt') as f:
    lines = f.readlines()

def part_one(all_games):
    blue = 14
    green = 13
    red = 12
    count = 0

    for idx, game in enumerate(all_games):
        game = game.strip("\n")
        
        start_idx = game.find(":")
        game_number = idx + 1
        games = game[start_idx+2:].split("; ")
        # print(games)
        possible = True 
        for game in games:
            # print(game)
            moves = game.split(", ")
            for move in moves:
                r = move.find(" red")
                g = move.find(" green")
                b = move.find(" blue")
                if r > 0:
                    c = int(move[:r])
                    if c > red:
                        possible = False 
                elif g > 0:
                    c = int(move[:g])
                    if c > green:
                        possible = False 
                elif b > 0:
                    c = int(move[:b])
                    if c > blue:
                        possible = False 

        if possible == True:
            count += game_number

    return count
        


def part_two(all_games):
    count = 0

    for game in all_games:
        game = game.strip("\n")
        start_idx = game.find(":")
        games = game[start_idx+2:].split("; ")
        blue = 0
        green = 0
        red = 0
        for game in games:
            # print(game)
            moves = game.split(", ")
            for move in moves:
                r = move.find(" red")
                g = move.find(" green")
                b = move.find(" blue")
                if r > 0:
                    c = int(move[:r])
                    if c > red:
                        red = c 
                elif g > 0:
                    c = int(move[:g])
                    if c > green:
                        green = c
                elif b > 0:
                    c = int(move[:b])
                    if c > blue:
                        blue = c  

        count += (red * blue * green)
    return count
        
        


print(part_one(lines))
print(part_two(lines))

