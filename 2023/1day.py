with open('1inp.txt') as f:
    lines = f.readlines()


def part_one(lines):
    count = 0
    for code in lines:
        line = code.strip("\n")
        backwards = line[::-1]
        i = 0
        first_num = -1
        second_num = -1
        while first_num < 0 or second_num < 0:
            if first_num < 0:
                try: 
                    first_num = int(line[i])
                except Exception:
                    first_num = -1 
            if second_num < 0:
                try:
                    second_num = int(backwards[i])
                except Exception:
                    second_num = -1 
            i += 1
        num = int(f'{first_num}{second_num}')
        count += num
            
    # print(count)
    return count 

# 4stonekdgdhxrtqv9sixonevhhmhqzp
def part_two(lines):
    count = 0
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for code in lines:
        code = code.strip("\n")
        idxs = {}
        i = 0
        while i < len(nums):
            idx = code.find(str(nums[i]))
            last_idx = code.rfind(str(nums[i]))
            if idx > -1:
                idxs[nums[i]] = [idx, last_idx]
            i += 1

        small = 1000
        large = -1
        for k, v in idxs.items():
            for idx in v:
                if idx < small:
                    small = idx 
                    small_val = k
                if idx > large:
                    large = idx 
                    large_val = k

        if type(small_val) == str:
            small_val = nums[nums.index(small_val) + 9]
        if type(large_val) == str:
            large_val = nums[nums.index(large_val) + 9]
        num = int(f'{small_val}{large_val}')

        count += num                
    return count
        

print(part_one(lines))
print(part_two(lines))

        