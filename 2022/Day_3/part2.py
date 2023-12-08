"""
Read every line from file.
Return: Array containing all the lines from the file.
"""


def read(filename):
    file = open(filename, "r")
    return file.readlines()


"""
Check for same character in strings.
Return: Character that appear in all three strings.
"""


def check_for_same(first, second, third):
    for char in first:
        if char == "\n":
            break
        if char in second:
            if char in third:
                return char
    return -1


# Initialize required variables
result = 0
dictionary = {}
lines = read("input.txt")


"""
Main. 
Return: Sum of the priorities of these item types.
"""


for i in range(26):
    dictionary[chr(97 + i)] = i + 1
for i in range(26):
    dictionary[chr(65 + i)] = i + 27
for i in range(0, len(lines), 3):
    first_line = lines[i]
    second_line = lines[i+1]
    third_line = lines[i+2]
    x = check_for_same(first_line, second_line, third_line)
    if x != -1:
        result += dictionary[x]
print(result)
