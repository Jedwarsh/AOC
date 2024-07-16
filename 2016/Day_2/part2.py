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

    if num_pad_pos == [1, 0]:
        x = 2
    elif num_pad_pos == [2, 0]:
        x = "D"
    elif num_pad_pos == [0, 1]:
        x = 4
    elif num_pad_pos == [1, 1]:
        x = "A"
    elif num_pad_pos == [2, 1]:
        x = "B"
    elif num_pad_pos == [0, 2]:
        x = 5
    elif num_pad_pos == [1, 2]:
        x = 6
    elif num_pad_pos == [1, 3]:
        x = 2
    elif num_pad_pos == [2, 2]:
        x = 7
    elif num_pad_pos == [2, 3]:
        x = 3
    elif num_pad_pos == [2, 4]:
        x = 1
    elif num_pad_pos == [3, 3]:
        x = 4
    elif num_pad_pos == [3, 2]:
        x = 8
    elif num_pad_pos == [3, 1]:
        x = "C"
    elif num_pad_pos == [4, 2]:
        x = 9
    return x


# Initialize required variables
result = ""
lines = read("input.txt")
prev_pos = [0, 2]
current_pos = [0, 2]
next_pos = [0, 2]
bad_pos = [[0, 0], [0, 1], [1, 0], [4, 4], [4, 3], [3, 4], [0, 4], [1, 4], [0, 3], [4, 0], [4, 1], [3, 0]]

"""
Main. 
Return: Bathroom code.
"""

for line in lines:
    for move in line:

        next_pos[0] = current_pos[0]
        next_pos[1] = current_pos[1]

        if move == "\n":
            break
        if move == "R":
            if current_pos[0] < 4:
                next_pos[0] += 1
        elif move == "L":
            if current_pos[0] > 0:
                next_pos[0] -= 1
        elif move == "U":
            if current_pos[1] < 4:
                next_pos[1] += 1
        elif move == "D":
            if current_pos[1] > 0:
                next_pos[1] -= 1

        if next_pos in bad_pos:
            current_pos[0] = prev_pos[0]
            current_pos[1] = prev_pos[1]
        else:
            current_pos[0] = next_pos[0]
            current_pos[1] = next_pos[1]
            prev_pos[0] = current_pos[0]
            prev_pos[1] = current_pos[1]

    result += (str(convert(current_pos)))

print(result)
