# first col is what opponent will play:
    #A rock, B paper, C scissors
# second col is what you should play
    # X rock, Y paper, Z scissors
# scoring:
    # rock = 1
    # paper = 2
    # scissors = 3
    # lose = 0
    # draw = 3
    # win = 6

import time 
score = 0

d = {
    "X": "A", 
    "Y": "B",
    "Z": "C"
} # converter

wins = {
    "A": "C",
    "B": "A",
    "C": "B"
}
losses = {
    "A": "B",
    "B": "C",
    "C": "A"
}
scoring = {
    "A": 1,
    "B": 2,
    "C": 3
}
second = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

t1 = time.time()
with open('2inp.txt') as f:
    lines = f.readlines()


for line in lines:
    l = d[line[2]]
    score += scoring[l]
    if line[0] == wins[l]:
        score += 6
    elif line[0] == losses[l]:
        pass 
    else:
        score += 3


t2 = time.time()
with open('2inp.txt') as f:
    lines = f.readlines()
new_score = 0



for line in lines:
    if line[2] == "X":
        letter = wins[line[0]]
        new_score += scoring[letter]
    elif line[2] == "Y":
        letter = line[0]
        new_score += scoring[line[0]] + 3
    elif line[2] == "Z":
        letter = losses[line[0]]
        new_score += scoring[letter] + 6

t3 = time.time()
print("Original score: ", score, t2-t1)
print("New score: ", new_score, t3-t2) 
