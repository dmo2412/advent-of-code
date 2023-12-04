# a = lowest, then b, ... up to z 
# S = current position
# E = position with best signal
# S has elevation of a and E has elevation z 
# import string
# with open('12inp.txt') as f:
#     lines = f.readlines()

# letters = {}

# for idx, i in enumerate(string.ascii_lowercase): 
#     letters[i] = idx + 1
# letters["S"] = 1
# letters["E"] = 100

# all_positions = []
# for idx, line in enumerate(lines):
#     line = line.strip("\n")
#     line = [*line]
#     all_positions.append(line)
#     if "E" in line:
#         e_row = idx
#         e_col = line.index("E")
#     if "S" in line:
#         s_row = idx
#         s_col = line.index("S")

# positions_dict = {}
# curr_pos = [s_row, s_col]
# e_pos = [e_row, e_col]
# for idx, line in enumerate(all_positions):
#     indices = [x for x in range(len(line))]
#     positions_dict[idx] = indices

# while curr_pos != e_pos:
#     moves = []
#     row = curr_pos[0]
#     col = curr_pos[1]
#     curr_letter = all_positions[row][col]
#     # print(curr_letter)
#     if row != 0:
#         up_row = row-1
#         moves.append([up_row, col])
        

# # e_pos = [e_row, e_col]
# # curr_pos = [s_row, s_col]
# # rows = len(all_positions)
# # columns = len(all_positions[0])
# # all_scores = []
# # for positions in all_positions:
# #     scores = []
# #     for letter in positions:
# #         scores.append(letters[letter])
# #     all_scores.append(scores)
# # print(all_scores)

# # move_count = 0
# # while curr_pos != e_pos:
# #     moves = []
# #     if curr_pos[0] != 0:





# # while curr_pos != e_pos:
# # for i in range(10):
# #     moves = []
# #     pos_letters = []
# #     diff = []
# #     scores = []
# #     # for i in range(4):
# #     curr_letter_score = letters[all_positions[curr_pos[0]][curr_pos[1]]]
# #     print(curr_letter_score)
# #     up = [curr_pos[0]-1, curr_pos[1]]
# #     down = [curr_pos[0]+1, curr_pos[1]]
# #     left = [curr_pos[0], curr_pos[1]-1]
# #     right = [curr_pos[0], curr_pos[1]+1]
        
# #     up_letter = all_positions[up[0]][up[1]]
# #     down_letter = all_positions[down[0]][down[1]]
# #     left_letter = all_positions[left[0]][left[1]]
# #     right_letter = all_positions[right[0]][right[1]]
# #     if curr_pos[0] != 0:
# #         moves.append(up)
# #         scores.append(letters[up_letter])
# #         pos_letters.append(up_letter)
# #         print("up")
# #     if curr_pos[0] != rows - 1:
# #         moves.append(down)
# #         scores.append(letters[down_letter])
# #         pos_letters.append(down_letter)
# #         print("down")
# #     if curr_pos[1] != 0:
# #         moves.append(left)
# #         scores.append(letters[left_letter])
# #         pos_letters.append(left_letter)
# #         print("left")
# #     if curr_pos[1] != columns - 1:
# #         moves.append(right)
# #         scores.append(letters[right_letter])
# #         pos_letters.append(right_letter)
# #         print("right")
# #     print(scores)
# #     print(pos_letters)
# #     break
    
    

    


