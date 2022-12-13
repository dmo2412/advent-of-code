from math import gcd
from functools import reduce
with open('11inp.txt') as f:
    lines = f.readlines()

monkeys = {
    0: {
        "starting_items": [77, 69, 76, 77, 50, 58],
        "operation": ["*", 11],
        "test": ["%", 5],
        "true": 1,
        "false": 5,
        "inspected": 0
    },
    1: {
        "starting_items": [75, 70, 82, 83, 96, 64, 62],
        "operation": ["+", 8],
        "test": ["%", 17],
        "true": 5,
        "false": 6,
        "inspected": 0
    },
    2: {
        "starting_items": [53],
        "operation": ["*", 3],
        "test": ["%", 2],
        "true": 0,
        "false": 7,
        "inspected": 0
    },
    3: {
        "starting_items": [85, 64, 93, 64, 99],
        "operation": ["+", 4],
        "test": ["%", 7],
        "true": 7,
        "false": 2,
        "inspected": 0
    },
    4: {
        "starting_items": [61, 92, 71],
        "operation": ["*", "old"],
        "test": ["%", 3],
        "true": 2,
        "false": 3,
        "inspected": 0
    },
    5: {
        "starting_items": [79, 73, 50, 90],
        "operation": ["+", 2],
        "test": ["%", 11],
        "true": 4,
        "false": 6,
        "inspected": 0
    },
    6: {
        "starting_items": [50, 89],
        "operation": ["+", 3],
        "test": ["%", 13],
        "true": 4,
        "false": 3,
        "inspected": 0
    },
    7: {
        "starting_items": [83, 56, 64, 58, 93, 91, 56, 65],
        "operation": ["+", 5],
        "test": ["%", 19],
        "true": 1,
        "false": 0,
        "inspected": 0
    }
}


# monkeys = {
#     0: {
#         "starting_items": [79, 98],
#         "operation": ["*", 19],
#         "test": ["%", 23],
#         "true": 2,
#         "false": 3,
#         "inspected": 0
#     },
#     1: {
#         "starting_items": [54, 65, 75, 74],
#         "operation": ["+", 6],
#         "test": ["%", 19],
#         "true": 2,
#         "false": 0,
#         "inspected": 0
#     },
#     2: {
#         "starting_items": [79, 60, 97],
#         "operation": ["*", "old"],
#         "test": ["%", 13],
#         "true": 1,
#         "false": 3,
#         "inspected": 0
#     },
#     3: {
#         "starting_items": [74],
#         "operation": ["+", 3],
#         "test": ["%", 17],
#         "true": 0,
#         "false": 1,
#         "inspected": 0
#     },
# }


def handle_reduce(items):
    empties = [1,2]
    if len(items) in empties:
        return items 
    else:
        x = reduce(gcd, items)
    result_items = []
    for i in items:
        result_items.append(i//x)
    return result_items

def handle_factoring(items):
    denominator = 20
    
    result_items = []
    while denominator < 20:
        for item in items:
            if item % denominator == 0:
                result_items.append(item / denominator)
                if len(result_items) == len(items):
                    return result_items
            else:
                result_items = []
                break
        denominator -= 1
    return items
    



def handle_operation(item, operation, test):
    if operation[0] == "*":
        if operation[1] == "old":
            worry = item * item
        else:
            worry = item * operation[1]
    else:
        worry = item + operation[1]
    # worry = handle_factoring(worry)
    return int(worry)

def handle_test(worry, divisor):
    if worry % divisor == 0:
        return "true"
    else:
        return "false"
    
def lcd(items, test):
    lcd_nums = []
        # print(worry, test)
    for item in items:
        lcd_nums.append(item % test)
    return lcd_nums

test_lcm = 1
for monkey, business in monkeys.items():
    test_lcm = test_lcm * business["test"][1]

for round in range(10000):
    for monkey, business in monkeys.items():
        # starting_items = lcd(business["starting_items"], business["test"][1])
        for item in business["starting_items"]:
            worry = handle_operation(item, business["operation"], business["test"][1])
            worry_test = handle_test(worry, business["test"][1])
            monkey_id = business[worry_test]
            worry = worry % test_lcm
            # worry_level = worry % business["test"][1]
            monkeys[monkey_id]["starting_items"].append(worry)
            monkeys[monkey]["inspected"] += 1
        monkeys[monkey]["starting_items"] = []

top = 0
second = 0

for k, v in monkeys.items():
    if v["inspected"] > top:
        second = top
        top = v["inspected"]
    elif v["inspected"] > second:
        second = v["inspected"]
    print(v["inspected"])

print(f"Part One: {top * second}")
# print(monkeys)
# print(top, second)


# Part Two










        
        


