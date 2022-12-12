with open('7inp.txt') as f:
    lines = f.readlines()

paths = {}
curr_path = ["start"]
curr_path_total = 0

for idx, line in enumerate(lines[1:]):
    line = line.strip("\n")
    commands = line.split(" ")
    
    if commands[0] == "dir":
        curr_path.append(commands[1])
        dir_path =  "/".join(curr_path)
        paths[dir_path] = []
        curr_path.pop()
    elif commands[0] != "$":
        dir_path = "/".join(curr_path)
        if dir_path not in paths:
            paths[dir_path] = [commands[0]]
        else:
            paths[dir_path].append(commands[0])
        tmp = []
        while len(curr_path) > 1:
            tmp.append(curr_path.pop())
            paths["/".join(curr_path)].append(commands[0])
        while len(tmp) > 0:
            curr_path.append(tmp.pop())
    elif commands[1] == "ls":
        pass
    elif commands[0] == "$" and commands[2] == "..":
        curr_path.pop()
    else:
        curr_path.append(commands[2])

total = 0
for k, v in paths.items():
    inner_total = 0
    for val in v:
        inner_total += int(val)
    if inner_total < 100000:
        total += inner_total
# print(total)
# print(paths)
# Part Two
used_space = 0
closest_dir = float("inf")

for space in paths["start"]:
    used_space += int(space)

needed_space = used_space - 40000000

for path, size in paths.items():
    path_space = sum([int(x) for x in size])
    if path_space > needed_space and path_space < closest_dir:
        closest_dir = path_space

print(closest_dir)
longest = ""
for k, v in paths.items():
    if len(k.split("/")) > len(longest.split("/")):
        longest = k
print(longest)