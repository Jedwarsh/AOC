# Importing needed modules
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
    all_number = []
    nums = re.finditer(r'\b(?:[0-9]\d{0,15}|999999999999999)\b', string)
    for m in nums:
        all_number.append(m.group())
    all_number = [eval(num) for num in all_number]
    return all_number


# Initialize required variables
lines = read("input.txt")
dictionaries = []
dict_counter = -1
smallest_location = 9999999999


"""
Main. 
Return: Smallest location that corresponds to any seed
"""


for line in lines:
    if line == "\n":
        dictionaries.append([])
        continue
    elif line[:6] == "seeds:":
        seeds = find_numbers(line)
        continue
    numbers = find_numbers(line)
    if len(numbers) < 1:
        continue
    dictionaries[-1].append(numbers)


for x in seeds:
    for i in range(7):
        for j in range(len(dictionaries[i])):
            padding = dictionaries[i][j][2]
            start = dictionaries[i][j][1]
            destination = dictionaries[i][j][0]
            if start <= x <= start + padding:
                if start > destination:
                    x = x - (start - destination)
                    break
                else:
                    x = x + (destination - start)
                    break
            else:
                x = x

    if x < smallest_location:
        smallest_location = x
print(smallest_location)


