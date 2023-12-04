# Read lines from file
file1 = open('input.txt', 'r')
lines = file1.readlines()

# Initialize required variables
counter = 0
draws = []
cubes = {"red": "12",
         "green": "13",
         "blue": "14"}
game_id = []


"""
Compare the set of cubes to the maximum set of cubes
Return: True or False based on if the set is possible or not
"""


def compare(hand_dict):
    for key, value in cubes.items():
        if key in hand_dict:
            if int(hand_dict[key]) > int(value):
                return False
    return True


"""
Divide the game into sets
Return: True or False based on the compare() function
"""


def divide_game(full_hand):
    for items in full_hand:
        items = items.split(" ")
        items.pop(0)
        hand = {}
        for i in range(0, len(items), 2):
            items[i+1] = items[i+1].replace(",", "")
            hand[items[i+1]] = items[i]
        if not compare(hand):
            return False
    return True


"""
Main 
Return: Sum of IDs
"""


for line in lines:
    line = line[:-1]
    line = line.split(":")
    game_id = line[0].split(" ")[1]
    draws = line[1]
    draws = draws.split(";")
    if not divide_game(draws):
        continue
    counter += int(game_id)
print(counter)
