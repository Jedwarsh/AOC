"""
Read every line from file.
Return: Array containing all the lines from the file.
"""


def read(filename):
    file = open(filename, "r")
    return file.readlines()


"""
Convert number
Return: Number.
"""


def convert(num_pad_pos):
    if num_pad_pos == [0, 0]:
        x = 1
    elif num_pad_pos == [1, 0]:
        x = 2
    elif num_pad_pos == [2, 0]:
        x = 3
    elif num_pad_pos == [0, 1]:
        x = 4
    elif num_pad_pos == [1, 1]:
        x = 5
    elif num_pad_pos == [2, 1]:
        x = 6
    elif num_pad_pos == [0, 2]:
        x = 7
    elif num_pad_pos == [1, 2]:
        x = 8
    elif num_pad_pos == [2, 2]:
        x = 9
    return x


# Initialize required variables
result = ""
lines = read("input.txt")
current_pos = [1, 1]

"""
Main. 
Return: Bathroom code.
"""

for line in lines:
    for move in line:
        if move == "R":
            if current_pos[0] < 2:
                current_pos[0] += 1
        elif move == "L":
            if current_pos[0] > 0:
                current_pos[0] -= 1
        elif move == "U":
            if current_pos[1] > 0:
                current_pos[1] -= 1
        elif move == "D":
            if current_pos[1] < 2:
                current_pos[1] += 1

    result += (str(convert(current_pos)))

print(result)
