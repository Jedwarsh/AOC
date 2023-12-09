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


# Initialize required variables
result = 0
lines = read("input.txt")

"""
Main. 
Return: Sum of these extrapolated values at the start.
"""


for line in lines:
    line = find_numbers(line)
    line.reverse()
    new_line = []
    counter = 0
    while True:
        counter += 1
        new_line.append([])
        if counter < 2:
            for index in range(1, len(line) - (counter - 1)):
                new_line[counter-1].append((line[index] - line[index - 1]))
        else:
            for index in range(1, len(new_line[counter-2])):
                new_line[counter-1].append((new_line[counter - 2][index] - new_line[counter - 2][index - 1]))
        if sum(new_line[-1]) == 0:
            (new_line[-1].append(0))
            for index in range(len(new_line) - 1, 0, -1):
                new_line[index-1].append(new_line[index-1][-1]+new_line[index][-1])
            break
    line.append(line[-1] + new_line[0][-1])
    result += line[-1]
print(result)

