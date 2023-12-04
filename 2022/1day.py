with open('inp.txt') as f:
    lines = f.readlines()

count = 0
top = 0
pos = 0
curr_pos = 1
for el in lines:
    x = el.find("\n")
    if x != 0:
        num = int(el[:x])
        count += num 
    else:
        if count > top:
            top = count 
            pos = curr_pos
        curr_pos += 1
        count = 0
        
print(top, pos)


# part two

# arr = [1,2,5,3,4]
# x = sorted(arr, reverse=True)
# print(x)
arr = [0,0,0]
count = 0
for el in lines:
    x = el.find("\n")
    if x != 0:
        num = int(el[:x])
        count += num
    else:
        if count > arr[0]:
            arr[0] = count
            arr = sorted(arr)
        count = 0
print(sum(arr))
