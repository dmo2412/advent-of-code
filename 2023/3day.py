with open('3inp.txt') as f:
    lines = f.readlines()

def part_one(lines):
    # 140 characters each line
    total = 0
    all_nums = []
    symbols = []
    for line_num, line in enumerate(lines):
        line = line.strip("\n")
        status = True 
        curr_num = ""
        for idx, char in enumerate(line):
            try:
                num = int(char)
                curr_num += char 
                status = True
            except Exception:
                if char != ".":
                    symbols.append(idx + (line_num * len(line)))
                if curr_num != "":
                    nums_idxs = len(curr_num)
                    nums = [i + (140 * line_num) for i in range(idx-nums_idxs, idx)]
                    all_nums.append({curr_num: nums})
                curr_num = "" 
                status = False 
        if status == True:
            x = len(curr_num)
            nums = [i + (140 * line_num) for i in range(140-x, 140)]
            all_nums.append({curr_num: nums})

    for values in all_nums:
        status = False  
        for key, val in values.items():
            for v in val:
                if status == True:
                    break
                acceptable = [int(v)+1, int(v)-1, int(v)-140, int(v)-141, int(v)-139, int(v)+140, int(v)+141, int(v)+139]
                for num in acceptable:
                    if num in symbols: 
                        total += int(key)
                        status = True 
                        break 

    return total
    # bad = "1234567890*&@/+#$%=-_"


def part_two(lines):
    total = 0
    all_nums = []
    stars = {}
    for line_num, line in enumerate(lines):
        line = line.strip("\n")
        status = True 
        curr_num = ""
        for idx, char in enumerate(line):
            try:
                num = int(char)
                curr_num += char 
                status = True
            except Exception:
                if char == "*":
                    stars[idx + (line_num * len(line))] = False
                if curr_num != "":
                    nums_idxs = len(curr_num)
                    nums = [i + (140 * line_num) for i in range(idx-nums_idxs, idx)]
                    all_nums.append({curr_num: nums})
                curr_num = "" 
                status = False 
        if status == True:
            x = len(curr_num)
            nums = [i + (140 * line_num) for i in range(140-x, 140)]
            all_nums.append({curr_num: nums})


    adjacents = {}

    for values in all_nums:
        status = False
        for key, val in values.items():
            for v in val:
                if status == True:
                    break
                acceptable = [int(v)+1, int(v)-1, int(v)-140, int(v)-141, int(v)-139, int(v)+140, int(v)+141, int(v)+139]
                for num in acceptable:
                    if num in stars:
                        if num in adjacents:
                            adjacents[num].append(int(key))
                        else:
                            adjacents[num] = [int(key)] 
                        status = True 
                        break 

    for k, v in adjacents.items():
        if len(v) == 2:
            print(v[0], v[1])
            total += v[0] * v[1]
        elif len(v) > 2:
            print(k, v)
    return total


print(part_one(lines))
print(part_two(lines))
