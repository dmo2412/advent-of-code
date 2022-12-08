with open('8inp.txt') as f:
    lines = f.readlines()

tree_map = {}
area_tracker = {}
vertical_trees = []
horizontal_trees = []

for idx, line in enumerate(lines):
    line = line.strip("\n")
    i = 0
    inner_tree_array = []
    while i < len(line):
        tree_idx = f"row-{idx+1} col-{i+1}"
        if idx == 0:
            vertical_trees.append([[tree_idx, line[i]]])
        else:
            vertical_trees[i].append([tree_idx, line[i]])
        
        inner_tree_array.append([tree_idx, line[i]])
        i += 1
    horizontal_trees.append(inner_tree_array)

for idx, trees in enumerate(horizontal_trees):
    for tree in trees:
        if idx == 0 or idx == len(trees)-1:
            tree_map[tree[0]] = 0
            area_tracker[tree[0]] = 0
for idx, trees in enumerate(vertical_trees):
    for tree in trees:
        if idx == 0 or idx == len(trees)-1:
            tree_map[tree[0]] = 0
            area_tracker[tree[0]] = 0


for idx, tree_line in enumerate(horizontal_trees):
    top_left = tree_line[0][1]
    i = 0
    high_i = 1
    while i < len(tree_line):
        if tree_line[i][1] > top_left:
            top_left = tree_line[i][1]
            if tree_line[i][0] in tree_map:
                tree_map[tree_line[i][0]] = 1
            else:
                tree_map[tree_line[i][0]] = 1
        
        curr_idx = i -1
        area_count = 0
        while curr_idx >= 0:
            if tree_line[curr_idx][1] < tree_line[i][1]:
                area_count += 1
                curr_idx -= 1
            else:
                area_count += 1
                break
        if tree_line[i][0] in area_tracker:
            area_tracker[tree_line[i][0]] *= area_count
        else:
            area_tracker[tree_line[i][0]] = area_count

        i += 1
    
    top_right = tree_line[-1][1]
    i = len(tree_line) - 1
    while i >= 0:
        if tree_line[i][1] > top_right:
            top_right = tree_line[i][1]
            if tree_line[i][0] in tree_map:
                tree_map[tree_line[i][0]] = (i - high_i) * tree_map[tree_line[i][0]]
            else:
                tree_map[tree_line[i][0]] = i - high_i
        
        curr_idx = i + 1
        area_count = 0
        while curr_idx < len(tree_line):
            if tree_line[curr_idx][1] < tree_line[i][1]:
                area_count += 1
                curr_idx += 1
            else:
                area_count += 1
                break
        if tree_line[i][0] in area_tracker:
            area_tracker[tree_line[i][0]] *= area_count
        else:
            area_tracker[tree_line[i][0]] = area_count            
        
        i -= 1

for idx, tree_line in enumerate(vertical_trees):
    top_top = tree_line[0][1]
    i = 1
    while i < len(tree_line):
        if tree_line[i][1] > top_top:
            top_top = tree_line[i][1]
            if tree_line[i][0] in tree_map:
                tree_map[tree_line[i][0]] = (i - high_i) * tree_map[tree_line[i][0]]
            else:
                tree_map[tree_line[i][0]] = i - high_i
        
        curr_idx = i - 1
        area_count = 0
        while curr_idx >= 0:
            if tree_line[curr_idx][1] < tree_line[i][1]:
                area_count += 1
                curr_idx -= 1
            else:
                area_count += 1
                break
        if tree_line[i][0] in area_tracker:
            area_tracker[tree_line[i][0]] *= area_count
        else:
            area_tracker[tree_line[i][0]] = area_count
        
        i += 1

    top_bottom = tree_line[-1][1]
    i = len(tree_line) - 1
    while i >= 0:
        if tree_line[i][1] > top_bottom:
            top_bottom = tree_line[i][1]
            if tree_line[i][0] in tree_map:
                tree_map[tree_line[i][0]] = (i - high_i) * tree_map[tree_line[i][0]]
            else:
                tree_map[tree_line[i][0]] = i - high_i
        
        curr_idx = i + 1
        area_count = 0
        while curr_idx < len(tree_line):
            if tree_line[curr_idx][1] < tree_line[i][1]:
                area_count += 1
                curr_idx += 1
            else:
                area_count += 1
                break
        if tree_line[i][0] in area_tracker:
            area_tracker[tree_line[i][0]] *= area_count
        else:
            area_tracker[tree_line[i][0]] = area_count
        
        
        i -= 1

highest = 0

for k, v in area_tracker.items():
    if v > highest:
        highest = v
print(highest)
print(len(tree_map))
