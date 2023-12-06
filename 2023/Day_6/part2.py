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
Find number in the string.
Return: The number.
"""


def find_numbers(string):
    number = []
    nums = re.finditer(r'\b(?:[0-9]\d{0,15}|999999999999999)\b', string)
    for m in nums:
        number.append(m.group())
    number = ''.join(number)
    return int(number)


# Initialize required variables
lines = read("input.txt")
time = find_numbers(lines[0])
result = 1
distance = find_numbers(lines[1])


"""
Main. 
Return: How many ways you can beat the record.
"""


counter = 0
for x in range(14, time):
    current_time = time - x
    if x * current_time > distance:
        counter += 1

result *= counter
print(result)
