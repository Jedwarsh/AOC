"""
Read line from file.
Return: String of line from the file.
"""


def read(filename):
    file = open(filename, "r")
    return file.readline()


# Initialize required variables
line = read("input.txt")


"""
Main. 
Return: Number of characters needed to be processed before first start-of-packet marker.
"""


for index in range(3, len(line) + 1):
    x = line[index-4:index]
    if len(set(x)) == len(x) and index > 4:
        print(index)
        break
