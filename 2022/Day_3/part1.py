"""
Read every line from file.
Return: Array containing all the lines from the file.
"""


def read(filename):
    file = open(filename, "r")
    return file.readlines()


"""
Check for same character in strings.
Return: Character that appear in both strings.
"""


def check_for_same(first, second):
    duplicates = []
    for char in first:
        if char in second:
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
for line in lines:
    line_start = line[:len(line)//2]
    line_end = line[len(line)//2:]
    line_end = line_end.replace("\n", "")
    x = check_for_same(line_start, line_end)
    if x != -1:
        result += dictionary[x]
print(result)
