"""
Read every line from file.
Return: Array containing all the lines from the file.
"""


def read(filename):
    file = open(filename, "r")
    return file.readlines()


# Initialize required variables
lines = read("input.txt")
vowels = "aeiou"
bad_strings = ["ab", "cd", "pq", "xy"]
number_of_nice_strings = 0


"""
Main. 
Return: number of nice strings.
"""


for line in lines:
    vowel_counter = 0
    double_counter = 0
    prev_char = ""
    for char in line:
        if char in vowels:
            vowel_counter += 1
        if prev_char == char:
            double_counter += 1
        if prev_char + char in bad_strings:
            vowel_counter = 0
            double_counter = 0
            break
        prev_char = char
    if vowel_counter >= 3 and double_counter >= 1:
        number_of_nice_strings += 1
print(number_of_nice_strings)
