"""
Read line from file.
Return: line.
"""


def read(filename):
    file = open(filename, "r")
    return file.readline()


# Initialize required variables
line = read("input.txt")
current_position = [0, 0]
visited_houses = [[0, 0]]
number_of_houses = 1


"""
Main. 
Return: Number of houses visited.
"""

for char in line:
    if char == "^":
        current_position[1] += 1
    elif char == "<":
        current_position[0] -= 1
    elif char == "v":
        current_position[1] -= 1
    elif char == ">":
        current_position[0] += 1
    if current_position not in visited_houses:
        visited_houses.append([current_position[0], current_position[1]])
        number_of_houses += 1
print(number_of_houses)
