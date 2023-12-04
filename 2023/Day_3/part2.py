# Import needed modules
import re

# Initialize required variables
previous = None
counter = 0

"""
Compare Find every '*' and its index in the string.
Return: Array containing indices for '*'.
"""


def find_symbol_position(string):
    positions = ([i for i, x in enumerate(string) if x == '*'])
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


def check_line(every_line, symbol, value):
    gear_counter = 0
    saved_numbers = []
    for sing_line in every_line:
        for j in range(0, len(sing_line), 3):
            if abs(sing_line[j+1] - symbol) <= 1 or abs(sing_line[j+2] - symbol) <= 1:
                gear_counter += 1
                saved_numbers.append(sing_line[j])

    if gear_counter == 2:
        x = int(saved_numbers[0])
        y = int(saved_numbers[1])
        power = x * y
        return value + power
    return value


"""
Go though all the symbols for a single line.
Return: Updated value.
"""


def get_sum(symbols, prev_line, current_line, next_line):
    value = 0
    for i in range(len(symbols)):
        value = check_line([prev_line, current_line, next_line], symbols[i], value)
    return value


"""
Main. 
Return: Sum of the gears.
"""


with open("input.txt") as f:
    previous = None
    current = next(f).strip()
    for line in f:
        line = line.strip()
        if previous is None:
            prev_numbers = ""
        else:
            prev_numbers = find_numbers(previous)
        current_numbers = find_numbers(current)
        next_numbers = find_numbers(line)
        current_symbols = find_symbol_position(current)
        counter += get_sum(current_symbols, prev_numbers, current_numbers, next_numbers)
        previous = current
        current = line
    prev_numbers = find_numbers(previous)
    current_numbers= find_numbers(current)
    current_symbols = find_symbol_position(current)
    counter += get_sum(current_symbols, prev_numbers, current_numbers, "")
    print(counter)
