# Read lines from file
file1 = open('input.txt', 'r')
lines = file1.readlines()

# Initialize required variables
counter = 0
cubes = {"red": "0",
         "green": "0",
         "blue": "0"}

"""
Compare the set of cubes to fewest possible set of cubes and make changes if needed
Return: None
"""


def compare(hand_dict):
    for key, value in cubes.items():
        if key in hand_dict:
            if int(hand_dict[key]) > int(value):
                cubes[key] = hand_dict[key]


"""
Divide the game into sets
Return: None
"""


def divide_game(full_hand):
    for items in full_hand:
        items = items.split(" ")
        items.pop(0)
        hand = {}
        for i in range(0, len(items), 2):
            items[i+1] = items[i+1].replace(",", "")
            hand[items[i+1]] = items[i]
        compare(hand)


"""
Calculate the power of the set of cubes
Return: Power of the set
"""


def calculate(hand):
    result = 1
    for key, value in hand.items():
        result *= int(value)
    return result


"""
Main 
Return: Sum of every sets power
"""


for line in lines:
    for key, value in cubes.items():
        cubes[key] = "0"
    line = line[:-1]
    line = line.split(":")
    game_id = line[0].split(" ")[1]
    draws = line[1]
    draws = draws.split(";")
    divide_game(draws)
    counter += calculate(cubes)
print(counter)