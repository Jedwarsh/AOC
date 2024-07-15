"""
Read every line from file.
Return: Array containing all the lines from the file.
"""


def read(filename):
    file = open(filename, "r")
    return file.readlines()


# Initialize required variables
result = 0
line = read("input.txt")
current_pos = [0, 0]
dirs = ["N", "E", "S", "W"]
current_dir = 0
line = line[0].split(", ")

"""
Main. 
Return: How far are we from the start.
"""

for move in line:

    if move[0] == "R":
        current_dir += 1
    elif move[0] == "L":
        current_dir -= 1

    current_dir = current_dir % 4

    if dirs[current_dir] == "N":
        current_pos[1] += int(move[1:])
    elif dirs[current_dir] == "S":
        current_pos[1] -= int(move[1:])
    elif dirs[current_dir] == "E":
        current_pos[0] += int(move[1:])
    elif dirs[current_dir] == "W":
        current_pos[0] -= int(move[1:])

result = current_pos[0] + current_pos[1]
print(abs(result))
