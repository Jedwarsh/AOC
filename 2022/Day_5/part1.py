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
Combine last elements of lists.
Return: String created by last elements.
"""


def create_string(list_of_chars):
    string = ""
    for i in range(len(list_of_chars)):
        string += list_of_chars[i][-1]
    return string


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
length = len(lines[1])
stacks = [[] for _ in range(length//4)]


"""
Main. 
Return: Which crates are at the top.
"""


for index in range(len(lines)):
    if lines[index][:2] == " 1":
        for index2 in range(0, index):
            counter = 0
            for index3 in range(1, len(lines[0]), 4):
                if lines[index2][index3] != " ":
                    x = (index3 // 4)
                    y = lines[index2][index3]
                    stacks[x].append(y)
        for index2 in range(len(stacks)):
            stacks[index2].reverse()
    if lines[index][:4] == "move":
        move = find_numbers(lines[index])
        for index2 in range(move[0]):
            x = stacks[move[2]-1]
            y = stacks[move[1]-1][-1]
            stacks[move[2] - 1].append(stacks[move[1] - 1][-1])
            stacks[move[1] - 1].pop()
print(create_string(stacks))
