"""
Read every line from file.
Return: Array containing all the lines from the file.
"""


def read(filename):
    file = open(filename, "r")
    return file.readlines()


# Initialize required variables
lines = read("input.txt")
counter = 1
score = 0
value = 1
lines = [s.replace('\n', '') for s in lines]
i = -1
x = True
wait = False
screen = ["."] * 240

"""
Main. 
Return: Print out the screen.
"""

while x:
    if counter < 240:
        if counter % 40 == value or counter % 40 == value + 1 or counter % 40 == value + 2:
            screen[counter - 1] = "#"
        else:
            screen[counter - 1] = "."
    if wait:
        counter += 1
        wait = False
        value += int(line[1])
        continue
    i += 1
    if i == len(lines):
        break
    line = lines[i].split(" ")
    if len(line) == 2:
        counter += 1
        wait = True
    else:
        counter += 1
    final_screen = [screen[i:i + 40] for i in range(0, len(screen), 40)]
print(final_screen)
