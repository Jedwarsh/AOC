"""
Read every line from file.
Return: Array containing all the lines from the file.
"""


def read(filename):
    file = open(filename, "r")
    return file.readlines()


# Initialize required variables
result = 0
highest_results = []
lines = read("input.txt")


"""
Main. 
Return: The most calories carried by any elf.
"""


for line in lines:
    if line == '\n':
        highest_results.append(result)
        result = 0
    else:
        result += int(line)
highest_results.append(result)
print(sorted(highest_results)[-1])
