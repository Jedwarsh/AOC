# Import needed modules
from shapely.geometry import Polygon


"""
Read every line from file.
Return: Array containing all the lines from the file.
"""


def read(filename):
    file = open(filename, "r")
    return file.readlines()


"""
Checks which side is viable path if there is one.
Return: Viable path if ther is one else returns False.
"""


def check_sides(x_pos, y_pos, strings):
    if strings[y_pos][x_pos + 1] == "J" or strings[y_pos][x_pos + 1] == "7" or strings[y_pos][x_pos + 1] == "-":
        return y_pos, x_pos + 1
    elif strings[y_pos][x_pos - 1] == "F" or strings[y_pos][x_pos - 1] == "L" or strings[y_pos][x_pos - 1] == "-":
        return y_pos, x_pos - 1
    elif strings[y_pos - 1][x_pos] == "F" or strings[y_pos - 1][x_pos] == "7" or strings[y_pos - 1][x_pos] == "|":
        return y_pos - 1, x_pos
    elif strings[y_pos + 1][x_pos] == "L" or strings[y_pos + 1][x_pos] == "J" or strings[y_pos + 1][x_pos] == "|":
        return y_pos + 1, x_pos


"""
Find starting position.
Return: X and Y coordinates.
"""


def find_start(strings):
    for index in range(len(strings)):
        for index2 in range(len(strings[index])):
            if strings[index][index2] == "S":
                return index, index2


# Initialize required variables
lines = read("input.txt")
counter = 1
y, x = find_start(lines)
current = lines[y][x]
next_y, next_x = check_sides(x, y, lines)
fence_coordinates = []


"""
Main. (ChatGPT and Reddit help)
Return: Number of tiles inside the fence.
"""


while True:
    fence_coordinates.append([x, y])
    if lines[next_y][next_x] == "S":
        counter + 1
        lines[next_y] = lines[next_y][:next_x] + "X" + lines[next_y][next_x + 1:]
        break
    if lines[next_y][next_x] == "-":
        a = next_x - x
        b = next_y - y
        x = next_x
        y = next_y
        if a == 1:
            next_x += 1
        else:
            next_x -= 1
        current = lines[y][x]
    elif lines[next_y][next_x] == "7":
        a = next_x - x
        b = next_y - y
        x = next_x
        y = next_y
        if a == 1:
            next_y += 1
        else:
            next_x -= 1
        current = lines[y][x]
    elif lines[next_y][next_x] == "|":
        a = next_x - x
        b = next_y - y
        x = next_x
        y = next_y
        if b > 0:
            next_y += 1
        else:
            next_y -= 1
        current = lines[y][x]
    elif lines[next_y][next_x] == "J":
        a = next_x - x
        b = next_y - y
        x = next_x
        y = next_y
        if a == 1:
            next_y -= 1
        else:
            next_x -= 1
        current = lines[y][x]
    elif lines[next_y][next_x] == "F":
        a = next_x - x
        b = next_y - y
        x = next_x
        y = next_y
        if a == -1:
            next_y += 1
        else:
            next_x += 1
        current = lines[y][x]
    elif lines[next_y][next_x] == "L":
        a = next_x - x
        b = next_y - y
        x = next_x
        y = next_y
        if a == -1:
            next_y -= 1
        else:
            next_x += 1
        current = lines[y][x]
    lines[y] = lines[y][:x] + "X" + lines[y][x + 1:]
    counter += 1
polygon = Polygon(fence_coordinates)
area_inside = polygon.area
i = area_inside - counter//2 + 1
print(i)
