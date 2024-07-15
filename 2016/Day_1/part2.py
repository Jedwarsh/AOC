"""
Read every line from file.
Return: Array containing all the lines from the file.
"""


def read(filename):
    file = open(filename, "r")
    return file.readlines()


"""
Append every visited square
Return: Nothing
"""


def move_it(x, direction, mode, state):
    for i in range(x):
        if mode == "+" and direction == "Y":
            current_pos[1] += 1
        elif mode == "-" and direction == "Y":
            current_pos[1] -= 1
        elif mode == "+" and direction == "X":
            current_pos[0] += 1
        elif mode == "-" and direction == "X":
            current_pos[0] -= 1
        xy = [current_pos[0], current_pos[1]]
        if xy in visited:
            result = current_pos[0] + current_pos[1]
            print(abs(result))
            return 1
        visited.append(xy)
    return 0


# Initialize required variables
line = read("input.txt")
found = 0
current_pos = [0, 0]
dirs = ["N", "E", "S", "W"]
current_dir = 0
visited = [[0, 0]]
line = line[0].split(", ")

"""
Main. 
Return: How many blocks away is the first location you visit twice.
"""

for move in line:

    if found == 1:
        break

    if move[0] == "R":
        current_dir += 1
    elif move[0] == "L":
        current_dir -= 1

    current_dir = current_dir % 4

    if dirs[current_dir] == "N":
        found = move_it(int(move[1:]), "Y", "+", found)
    elif dirs[current_dir] == "S":
        found = move_it(int(move[1:]), "Y", "-", found)
    elif dirs[current_dir] == "E":
        found = move_it(int(move[1:]), "X", "+", found)
    elif dirs[current_dir] == "W":
        found = move_it(int(move[1:]), "X", "-", found)



