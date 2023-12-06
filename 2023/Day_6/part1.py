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
    nums = re.finditer(r'\b(?:[0-9]\d{0,15}|999999999999999)\b', string)
    for m in nums:
        all_number.append(m.group())
    all_number = [eval(num) for num in all_number]
    return all_number


# Initialize required variables
lines = read("input.txt")
time = find_numbers(lines[0])
result = 1
distance = find_numbers(lines[1])


"""
Main. 
Return: Number of ways you can beat the record multiplied together.
"""


for game_number in range(len(distance)):
    counter = 0
    game_time = time[game_number]
    game_distance = distance[game_number]
    for x in range(game_time):
        current_time = game_time - x
        if x * current_time > game_distance:
            counter += 1

    result *= counter
print(result)
