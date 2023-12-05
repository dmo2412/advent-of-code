with open('4inp.txt') as f:
    lines = f.readlines()


def part_one(lines):
    points = 0

    for line in lines:
        line = line.strip("\n")
        start = line.find(":")
        nums = line[start+1:].split("|")
        winners = nums[0].split(" ")
        winning_nums = [int(i) for i in winners if i != '']
        yours = nums[1].split(" ")
        your_nums = [int(i) for i in yours if i != '']
        
        curr_points = 0
        for num in your_nums:
            if num in winning_nums:
                # print(num)
                if curr_points == 0:
                    curr_points = 1
                else:
                    curr_points *= 2
        points += curr_points
    return points


def part_two(lines):
    cards = {}

    for i in range(len(lines)):
        cards[i+1] = 1


    for idx, line in enumerate(lines):
        line = line.strip("\n")
        start = line.find(":")
        nums = line[start+1:].split("|")
        winners = nums[0].split(" ")
        winning_nums = [int(i) for i in winners if i != '']
        yours = nums[1].split(" ")
        your_nums = [int(i) for i in yours if i != '']
        winners_on_card = 0
        current_cards = cards[idx + 1]

        for num in your_nums:
            if num in winning_nums:
                winners_on_card += 1
        
        cards = fill_card(cards, idx+1, winners_on_card, current_cards)

    count = 0
    for k, v in cards.items():
        count += v
    return count

         


def fill_card(cards, idx, winners, current_cards):
    for i in range(idx + 1, idx + winners + 1):
        cards[i] += current_cards 
    return cards 



print(part_one(lines))
print(part_two(lines))
# 1081 is too low
# 3455531407 is too high
# 957473979
# 996574