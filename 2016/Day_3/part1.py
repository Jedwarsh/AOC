"""
Read every line from file.
Return: Array containing all the lines from the file.
"""


def read(filename):
    file = open(filename, "r")
    return file.readlines()


"""
Compare sides of triangle.
Return: True or False.
"""


def compare_triangle(numbers):
    if (int(numbers[0]) + int(numbers[1])) <= int(numbers[2]):
        return False
    elif (int(numbers[0]) + int(numbers[2])) <= int(numbers[1]):
        return False
    elif (int(numbers[2]) + int(numbers[1])) <= int(numbers[0]):
        return False
    return True


# Initialize required variables
result = 0
lines = read("input.txt")

"""
Main. 
Return: Number of viable triangles.
"""

for line in lines:
    line = line.strip()
    line = line.split(" ")
    line = list(filter(None, line))
    if compare_triangle(line):
        result += 1
print(result)
