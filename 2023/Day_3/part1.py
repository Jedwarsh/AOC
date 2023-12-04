# Import needed modules
import re

# Initialize required variables
previous = None
counter = 0

"""
Compare Find every symbol that is not a '0' or a digit and its index in the string.
Return: Array containing indices for symbols.
"""


def find_symbol_position(string):
    positions = ([i for i, x in enumerate(string) if not x.isdigit() and x != '.'])
    return positions


"""
Find every number in the string.
Return: Array containing the number its starting index and the last characters index.
"""


def find_numbers(string):
    all_number = []
    numbers = re.finditer(r'\b(?:[1-9]\d{0,2}|999)\b', string)
    for m in numbers:
        all_number.append(m.group())
        all_number.append(m.start())
        all_number.append(m.end()-1)
    return all_number


"""
Check if the symbol is relevant for our calculation or not.
If its relevant calculate.
Return: Updated value.
"""


def check_line(every_line, number, start, end, value):
    for sing_line in every_line:
        for j in sing_line:
            if start <= j-1 <= end or start <= j <= end or start <= j+1 <= end:
                return value+int(number)
    return value


"""
Go though all the numbers for a single line.
Return: Updated value.
"""


def get_sum(numbers, prev_line, current_line, next_line):
    value = 0
    for i in range(len(numbers)):
        if i % 3 == 0:
            value = check_line([prev_line, current_line, next_line], numbers[i], numbers[i+1], numbers[i+2], value)
    return value


"""
Main. 
Return: Sum of the numbers adjacent to symbols.
"""


with open("input.txt") as f:
    previous = None
    current = next(f).strip()
    for line in f:
        line = line.strip()
        if previous is None:
            prev_symbols = ""
        else:
            prev_symbols = find_symbol_position(previous)
        current_symbols = find_symbol_position(current)
        next_symbols = find_symbol_position(line)
        current_numbers = find_numbers(current)
        counter += get_sum(current_numbers, prev_symbols, current_symbols, next_symbols)
        previous = current
        current = line
    prev_symbols = find_symbol_position(previous)
    current_symbols = find_symbol_position(current)
    current_numbers = find_numbers(current)
    counter += get_sum(current_numbers, prev_symbols, current_symbols, "")
    print(counter)
