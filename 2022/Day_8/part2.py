"""
Read every line from file.
Return: Array containing all the lines from the file.
"""


def read(filename):
    file = open(filename, "r")
    return file.readlines()


"""
Find a bigger number to the right.
Return: Boolean or distance till higher tree
"""


def bigger_number_right(strings, x, y):
    counter = 0
    for z in range(y + 1, len(strings[0])):
        counter += 1
        if int(strings[x][z]) >= int(strings[x][y]):
            return True, counter
    return False, counter


"""
Find a bigger number to the left.
Return: Boolean or distance till higher tree
"""


def bigger_number_left(strings, x, y):
    counter = 0
    for z in reversed(range(0, y)):
        counter += 1
        if int(strings[x][z]) >= int(strings[x][y]):
            return True, counter
    return False, counter


"""
Find a bigger number to the top.
Return: Boolean or distance till higher tree
"""


def bigger_number_top(strings, x, y):
    counter = 0
    for z in reversed(range(0, x)):
        counter += 1
        if int(strings[z][y]) >= int(strings[x][y]):
            return True, counter
    return False, counter


"""
Find a bigger number to the bottom.
Return: Boolean or distance till higher tree
"""


def bigger_number_bottom(strings, x, y):
    counter = 0
    for z in range(x + 1, len(strings)):
        counter += 1
        if int(strings[z][y]) >= int(strings[x][y]):
            return True, counter
    return False, counter


# Initialize required variables
lines = read("input.txt")
score = 0
lines = [s.replace('\n', '') for s in lines]


"""
Main. 
Return: Highest scenic score for any tree.
"""

for i in range(len(lines)):
    for j in range(len(lines[0])):
        distance = [0, 0, 0, 0]
        if i == 0 or i == len(lines)-1 or j == 0 or j == len(lines[0])-1:
            continue
        if not bigger_number_right(lines, i, j):
            continue
        else:
            distance[0] = bigger_number_right(lines, i, j)[1]
        if not bigger_number_left(lines, i, j):
            continue
        else:
            distance[2] = bigger_number_left(lines, i, j)[1]
        if not bigger_number_top(lines, i, j):
            continue
        else:
            distance[3] = bigger_number_top(lines, i, j)[1]
        if not bigger_number_bottom(lines, i, j):
            continue
        else:
            distance[1] = bigger_number_bottom(lines, i, j)[1]
        scenic = distance[0]*distance[1]*distance[2]*distance[3]
        if scenic > score:
            score = scenic
print(score)
