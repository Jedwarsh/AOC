# Import needed modules
import numpy as np


""""
Read every line from file.
Return: Array containing all the lines from the file.
"""


def read(file_path, strings):
    with open(file_path, 'r') as file:
        for line in file:
            # Append each character in the line to the list
            string = list(line.strip())
            strings.append(string)
        return strings


"""
Expand array based on empty lines.
Return: New array.
"""


def expand(array, axis):
    index = 0
    while True:
        if axis == 1:
            x = array[:, index]
            x_set = set(array[:, index])
            new_array = np.full_like(x, "U", dtype=np.dtype('U'))
        else:
            x = array[index, :]
            x_set = set(array[index, :])
            new_array = np.full_like(x, "U", dtype=np.dtype('U'))
        if "#" not in x_set and axis == 1:
            array[:, index] = new_array
        elif "#" not in x_set and axis == 0:
            array[index, :] = new_array
        index += 1
        num_of_rows, num_of_columns = array.shape
        if index == num_of_columns and axis == 1:
            break
        if index == num_of_rows and axis == 0:
            break
    return array


# Initialize required variables

result = 0
rows = []
rows = read("input.txt", rows)
matrix = np.array(rows)
matrix = expand(matrix, 1)
matrix = expand(matrix, 0)
num_rows, num_columns = matrix.shape


"""
Main. 
Return: Sum of distance between all star pairs.
"""


for i in range(num_rows):
    for j in range(num_columns):
        if matrix[i][j] == "#":
            matrix[i][j] = "X"
            start = i + j
            for i2 in range(i, num_rows):
                if i2 == 0:
                    z = j + 1
                else:
                    z = 0
                for j2 in range(z, num_columns):
                    if matrix[i2][j2] == "#":
                        new_i = i - i2
                        new_j = j - j2
                        result += abs(i2 - i) + abs(j2 - j)
                        if new_i < 0:
                            k = -1
                        else:
                            k = 1
                        for f in range(i2, i + k, k):
                            if matrix[f][j2] == "U":
                                result += 999999
                        if new_j < 0:
                            k = -1
                        else:
                            k = 1
                        for f2 in range(j2, j + k, k):
                            if matrix[f][f2] == "U":
                                result += 999999
print(result)

