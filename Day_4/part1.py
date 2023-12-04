# Import needed modules
import re


"""
Read every line from file.
Return: Array containing all the lines from the file.
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
    id = string[0][5:]
    string = string[1]
    string = string.split("|")
    numbers_first_half = find_numbers(string[0])
    numbers_second_half = find_numbers(string[1])
    return [id, numbers_first_half, numbers_second_half]

# Initialize required variables
games = read("input.txt")
game_id = 0
counter = 0


"""
Main. 
Return: Number of total points based on the scratchcards
"""


for game in games:
    score = -1
    game_id, card_numbers, winner_numbers = split_game(game)
    for i in card_numbers:
        if i in winner_numbers:
            score += 1
    if score >= 0:
        counter += pow(2,score)
print(counter)
