# Import needed modules
import re


"""
Read every line from file.
Return: Array containing all the lines from the file.
"""


def read(filename):
    file = open(filename, "r")
    return file.readlines()


"""
Find every number in the string.
Return: Array containing the numbers.
"""


def find_numbers(string):
    return list(map(int, re.findall(r'-?\d+', string)))


"""
Converts the sizes of files
Return: None.
"""


def change_dict():
    items = list(dirs.values())
    keys = list(dirs.keys())
    for index in range(len(dirs)-1, -1, -1):
        if not all(isinstance(x, int) for x in items[index]):
            for index2 in items[index]:
                if index2 in dirs and len(dirs[keys[index]]) > 1:
                    x = dirs[keys[index]].index(index2)
                    dirs[keys[index]][x] = dirs[index2]
                elif index2 in dirs and len(dirs[keys[index]]) == 1:
                    dirs[keys[index]] = dirs[index2]
            if type(dirs[keys[index]]) is not int:
                dirs[keys[index]] = sum(items[index])
        else:
            dirs[keys[index]] = sum(items[index])


# Initialize required variables
lines = read("input.txt")
dirs = {}
score = 0
current_dir = ""
current_dir_elements = []
prev_dirs = []


"""
Main. 
Return: Total size of directory we should delete.
"""


for line in lines:
    if line[:7] == "$ cd ..":
        if len(prev_dirs) == 1:
            result = prev_dirs[0]
        else:
            result = prev_dirs[0] + "/".join(prev_dirs[1:])
        if len(current_dir_elements) > 0:
            dirs[result] = current_dir_elements
            current_dir_elements = []
        prev_dirs.pop()
        current_dir = prev_dirs[-1]
    elif line[:4] == "$ cd":
        if current_dir == "":
            current_dir = line.split()[-1]
            prev_dirs.extend(line.split()[-1])
        else:
            if len(prev_dirs) == 1:
                result = prev_dirs[0]
            else:
                result = prev_dirs[0] + "/".join(prev_dirs[1:])
            if len(current_dir_elements) > 0:
                dirs[result] = current_dir_elements
                current_dir_elements = []
            current_dir = line.split()[-1]
            prev_dirs.append(line.split()[-1])
    elif line[0] != "$":
        if len(find_numbers(line)) > 0:
            current_dir_elements.extend(find_numbers(line))
        else:
            if len(prev_dirs) == 1:
                result = prev_dirs[0]
            else:
                result = prev_dirs[0] + "/".join(prev_dirs[1:])
            if current_dir == "/":
                current_dir_elements.append(result + line.split()[-1])
            else:
                current_dir_elements.append(result + "/" + line.split()[-1])
if len(prev_dirs) == 1:
    result = prev_dirs[0]
else:
    result = prev_dirs[0] + "/".join(prev_dirs[1:])
dirs[result] = current_dir_elements
change_dict()
limit = 30000000 - (70000000 - dirs["/"])
smallest_dir = dirs["/"]
for directory in dirs.values():
    if limit < directory < smallest_dir:
        smallest_dir = directory
print(smallest_dir)
