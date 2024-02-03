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


"""
Main. 
Return: Sum of these six signal strengths.
"""

while x:
    if counter % 40 == 20:
        z = counter * value
        score += z
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

print(score)
