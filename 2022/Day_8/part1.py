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
    return list(map(int, re.findall(r'-?\d+', string)))


"""
Find a bigger number to the right.
Return: Boolean
"""


def bigger_number_right(strings, x, y):
    for z in range(y + 1, len(strings[0])):
        if int(strings[x][z]) >= int(strings[x][y]):
            return True
    return False


"""
Find a bigger number to the left.
Return: Boolean
"""


def bigger_number_left(strings, x, y):
    for z in reversed(range(0, y)):
        if int(strings[x][z]) >= int(strings[x][y]):
            return True
    return False


"""
Find a bigger number to the top.
Return: Boolean
"""


def bigger_number_top(strings, x, y):
    for z in reversed(range(0, x)):
        if int(strings[z][y]) >= int(strings[x][y]):
            return True
    return False


"""
Find a bigger number to the bottom.
Return: Boolean
"""


def bigger_number_bottom(strings, x, y):
    for z in range(x + 1, len(strings)):
        if int(strings[z][y]) >= int(strings[x][y]):
            return True
    return False


# Initialize required variables
lines = read("input.txt")
score = 0
lines = [s.replace('\n', '') for s in lines]


"""
Main. 
Return: Total numbers of visible trees.
"""

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if i == 0 or i == len(lines)-1 or j == 0 or j == len(lines[0])-1:
            score += 1
            continue
        if not bigger_number_right(lines, i, j):
            score += 1
            continue
        if not bigger_number_left(lines, i, j):
            score += 1
            continue
        if not bigger_number_top(lines, i, j):
            score += 1
            continue
        if not bigger_number_bottom(lines, i, j):
            score += 1
            continue
print(score)

