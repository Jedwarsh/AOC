# Import needed modules
import numpy as np


""""
Read every line from file.
Return: Array containing all the lines from the file.
"""


def read(file_path):
    with open(file_path, 'r') as file:
        strings = []
        for line in file:
            line = line[:-1]
            string = line.split("   ")
            strings.append(string)
        strings = np.array(strings)
        first_column = np.asfarray(strings[:, 0], int)
        second_column = np.asfarray(strings[:, 1], int)
        return first_column, second_column


first = []
second = []
first, second = read("input.txt")
first = np.sort(first)
second = np.sort(second)
output = 0
for i in range(len(first)):
    number_of = np.count_nonzero(second == first[i])
    output += number_of * first[i]
print(int(output))

