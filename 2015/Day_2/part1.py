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


# Initialize required variables
sizes = read("input.txt")


"""
Main. 
Return: The amount of paper needed in square feet
"""

sum_of_paper = 0
for line in sizes:
    line = line.replace("x", " ")
    line = find_numbers(line)
    line = [eval(i) for i in line]
    sides = [line[0] * line[1], line[1] * line[2], line[0] * line[2]]
    sides = sorted(sides)
    sum_of_paper += 2 * sides[0] + 2 * sides[1] + 2 * sides[2] + sides[0]
print(sum_of_paper)
