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
    else:
        return True


# Initialize required variables
result = 0
lines = read("input.txt")

"""
Main. 
Return: Number of viable triangles.
"""

for i in range(0, len(lines), 3):
    line1 = lines[i].strip()
    line1 = line1.split(" ")
    line1 = list(filter(None, line1))

    line2 = lines[i + 1].strip()
    line2 = line2.split(" ")
    line2 = list(filter(None, line2))

    line3 = lines[i + 2].strip()
    line3 = line3.split(" ")
    line3 = list(filter(None, line3))

    for j in range(3):
        nums = [line1[j], line2[j], line3[j]]
        if compare_triangle(nums):
            result += 1
print(result)
