# first value is called left
# second value is called right 
# if both integers, lower integer should come first
# if both values are lists, compare the first value of each list, then second and so on:
    # if leftlist runs out of items first, list is good. Same length = keep checking
# if one value is an integer, convert integer to list which contains that integer as its only value, then retry the comparison
def main(lines):
    left_packets = []
    right_packets = []
    for idx, line in enumerate(lines):
        line = line.strip("\n")
        if idx % 3 == 0:
            left_packets.append(eval(line))
        elif idx % 3 == 1:
            right_packets.append(eval(line))
    # for (left, right) in zip(left_packets, right_packets):
    #     compare(left, right)
    compare(left_packets[1], right_packets[1])
        


def compare(left, right):
    ans = flatten(left)
    print(ans)

def flatten(packet):
    flattened = []
    unflattened = []
    for piece in packet:
        if type(piece) == int:
            flattened.append([piece])
        elif type(piece) == list and len(piece) == 0:
            flattened.append(piece)
        else:
            print(piece)
            # return flatten(piece)

    return flattened





with open('13inp.txt') as f:
    lines = f.readlines()

main(lines)



# def separate_packet(packet):
#     open_bracket_indices = []
#     closed_bracket_indices = []

#     for idx, char in enumerate(packet):
#         if char == "[":
#             open_bracket_indices.append(idx)
#         elif char == "]":
#             closed_bracket_indices.append(idx)

#     x = break_down(packet, open_bracket_indices, closed_bracket_indices, [])
#     print(x)

# def get_new_indices(packet):
#     open_bracket_indices = []
#     closed_bracket_indices = []

#     for idx, char in enumerate(packet):
#         if char == "[":
#             open_bracket_indices.append(idx)
#         elif char == "]":
#             closed_bracket_indices.append(idx)

#     return open_bracket_indices, closed_bracket_indices


# def break_down(packet, open_bracket_indices, closed_bracket_indices, all_chunks):
#     left_idx = open_bracket_indices[-1]
#     open_bracket_indices.pop()
#     for idx, indice in enumerate(closed_bracket_indices):
#         if indice > left_idx:
#             right_idx = indice
#             pop_idx = idx 
#             break
#     chunk = packet[left_idx:right_idx+1]
#     all_chunks.append(eval(chunk))
#     # print(packet)
#     packet = packet[:left_idx-1] + packet[right_idx+1:]
#     open_bracket_indices, closed_bracket_indices = get_new_indices(packet)
#     # print(packet, chunk, all_chunks)
#     if len(open_bracket_indices) > 1:
#         return break_down(packet, open_bracket_indices, closed_bracket_indices, all_chunks)
#     else:
#         if packet[0] != "[":
#             packet = "[" + packet 
#         elif packet[-1] != "]":
#             packet += "]"
#         all_chunks.append(eval(packet))
#         return all_chunks
