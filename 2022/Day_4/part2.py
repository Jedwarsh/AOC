"""
Read every line from file.
Return: Array containing all the lines from the file.
"""


def read(filename):
    file = open(filename, "r")
    return file.readlines()


"""
Checks if one range overlaps the other,
Return: True or False
"""


def contains(begin, end):
    begin = [eval(i) for i in begin]
    end = [eval(i) for i in end]
    if (begin[0] >= end[0] and end[1] >= begin[1]) or (begin[0] <= end[0] and end[1] <= begin[1]):
        return 1
    elif end[0] <= begin[0] <= end[1] or begin[0] <= end[0] <= begin[1]:
        return 1
    return 0


# Initialize required variables
result = 0
lines = read("input.txt")


"""
Main. 
Return: The number of assignments where one overlaps the other.
"""


for line in lines:
    line = line.replace("\n", "")
    line = line.split(",")
    start = line[0].split("-")
    finish = line[1].split("-")
    if contains(start, finish):
        result += 1
print(result)
