"""
Read every line from file.
Return: Array containing all the lines from the file.
"""


def read(filename):
    file = open(filename, "r")
    return file.readlines()


# Initialize required variables
lines = read("input.txt")
number_of_nice_strings = 0


"""
Main. 
Return: number of nice strings.
"""


for line in lines:
    doubles = []
    double_counter = 0
    pair_counter = 0
    prev_char = ""
    prev_prev_char = ""
    prev_prev_prev_char = ""
    for char in line:
        if prev_prev_char == char:
            pair_counter += 1
        if prev_char != "":
            two = prev_char + char
            if two in doubles:
                if prev_prev_char == prev_char == char:
                    if prev_prev_prev_char == prev_prev_char == prev_char == char:
                        double_counter += 1
                else:
                    double_counter +=1
            else:
                doubles.append(prev_char+char)
        prev_prev_prev_char = prev_prev_char
        prev_prev_char = prev_char
        prev_char = char
    if double_counter >= 1 and pair_counter >= 1:
        number_of_nice_strings += 1
print(number_of_nice_strings)
