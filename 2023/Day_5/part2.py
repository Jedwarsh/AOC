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
Find every starting and ending number in the string.
Return: Array containing the start and ending numbers.
"""


def find_start_and_end_numbers(string):
    all_number = [[],[]]
    counter = 0
    nums = re.finditer(r'\b(?:[0-9]\d{0,15}|999999999999999)\b', string)
    for m in nums:
        if counter % 2 == 0:
            all_number[0].append(int(m.group()))
        else:
            all_number[1].append(int(m.group()))
        counter += 1
    return all_number


"""
Sort a list containing list of numbers based on the second value in the lists.
Return: Sorted list
"""


def sort_second(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if (sub_li[j][1] > sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j] = sub_li[j + 1]
                sub_li[j + 1] = tempo
    return sub_li


"""
Find next seed at the end of the range.
Return: Seed at the end of the range
"""


def find_end_range_for_same(strings, seed):
    strings = sort_second(strings)
    current = -1
    prev = -1
    if any(seed > element for sublist in strings for element in sublist):
        return seed+1
    for string in strings:
        if current != -1:
            prev = current
        current = string[1]
        if prev <= seed <= current:
            seed = current
    return seed


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
smallest_location = 9999999999999


"""
Main. 
Return: Smallest location that corresponds to any seed
"""


for line in lines:
    if line == "\n":
        dictionaries.append([])
        continue
    elif line[:6] == "seeds:":
        seeds_ranges = find_start_and_end_numbers(line)
        continue
    numbers = find_numbers(line)
    if len(numbers) < 1:
        continue
    dictionaries[-1].append(numbers)
for s in range(len(seeds_ranges[0])):
    seed_start = seeds_ranges[0][s]
    seed_end = seed_start + seeds_ranges[1][s]
    k = seed_start
    while seed_start <= k <= seed_end-1:
        x = k
        lowest_distance = [0, 0, 0, 0, 0, 0, 0]
        for i in range(7):
            y = 0
            for j in range(len(dictionaries[i])):
                padding = dictionaries[i][j][2]
                start = dictionaries[i][j][1]
                destination = dictionaries[i][j][0]
                if start <= x <= start + padding:
                    if start > destination:
                        y = x - (start - destination)
                        break
                    else:
                        y = x + (destination - start)
                        break
            if y == 0:
                x = x
                new_start = find_end_range_for_same(dictionaries[i], x)
                lowest_distance[i] = new_start
            else:
                x = y
                lowest_distance[i] = (destination + padding) - x
        lowest_distance = [x for x in lowest_distance]
        lowest_distance = sorted(lowest_distance)
        smallest = min(x for x in lowest_distance)
        if smallest < 1:
            smallest = 1
        if x < smallest_location:
            smallest_location = x
        k += smallest
print(smallest_location)



