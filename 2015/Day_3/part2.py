"""
Read line from file.
Return: line.
"""


def read(filename):
    file = open(filename, "r")
    return file.readline()


# Initialize required variables
line = read("input.txt")
current_position_santa = [0, 0]
current_position_robot = [0, 0]
visited_houses = [[0, 0]]
number_of_houses = 1


"""
Moves santa and checks the houses 
Return: New Position
"""


def move_santa(position, numbers):
    if char == "^":
        position[1] += 1
    elif char == "<":
        position[0] -= 1
    elif char == "v":
        position[1] -= 1
    elif char == ">":
        position[0] += 1
    if position not in visited_houses:
        visited_houses.append([position[0], position[1]])
        numbers += 1
    return position, numbers


"""
Main. 
Return: Number of houses visited.
"""


for i in range(len(line)):
    char = line[i]
    if i % 2 == 0:
        current_position_santa, number_of_houses = move_santa(current_position_santa, number_of_houses)
    else:
        current_position_robot, number_of_houses = move_santa(current_position_robot, number_of_houses)
print(number_of_houses)