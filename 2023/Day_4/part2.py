import re


"""
Read every line from file
Return: Array containing all the lines from the file
"""


def read(filename):
    file = open(filename, "r")
    return file.readlines()


"""
Find every number in the string.
Return: Array containing the numbers.
"""


def find_numbers(string):
    all_number = []
    numbers = re.finditer(r'\b(?:[1-9]\d{0,2}|999)\b', string)
    for m in numbers:
        all_number.append(m.group())
    return all_number


"""
Split the string into three parts.
Return: Array containing all three parts.
"""


def split_game(string):
    string = string.split(":")
    string = string[1]
    string = string.split("|")
    numbers_first_half = find_numbers(string[0])
    numbers_second_half = find_numbers(string[1])
    return [numbers_first_half, numbers_second_half]


# Initialize required variables
game_id = 0
games = read("input.txt")
k = 0


"""
Main. 
Return: Number of scratchcards
"""


for game in games:
    step = 0
    card_numbers, winner_numbers = split_game(game)
    for j in range(len(card_numbers)):
        number = card_numbers[j]
        if number in winner_numbers:
            games.append(games[int(game_id)+step])
            step += 1
    k += 1
print(len(games))
