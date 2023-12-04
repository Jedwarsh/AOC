"""
Read line from file
Return: line
"""


def read(filename):
    file = open(filename, "r")
    return file.readline()


# Initialize required variables
line = read("input.txt")
floor = 0


"""
Main. 
Return: Position where basement floor is reached
"""


for i in range(len(line)):
    char = line[i]
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1
    if floor == -1:
        print(i+1)
        break
