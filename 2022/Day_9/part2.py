"""
Read every line from file.
Return: Array containing all the lines from the file.
"""


def read(filename):
    file = open(filename, "r")
    return file.readlines()


"""
Make part of rope follow the previous one.
Return: Second part of the rope.
"""


def follow(head, tail):
    y = head[0] - tail[0]
    x = head[1] - tail[1]
    if abs(x) > 1:
        if y != 0:
            if y < 0:
                tail[0] -= 1
            else:
                tail[0] += 1
        if x < 0:
            tail[1] -= abs(x) - 1
            return tail
        else:
            tail[1] += abs(x) - 1
            return tail
    elif abs(y) > 1:
        if x != 0:
            if x < 0:
                tail[1] -= 1
            else:
                tail[1] += 1
        if y < 0:
            tail[0] -= abs(y) - 1
            return tail
        else:
            tail[0] += abs(y) - 1
            return tail
    return False


"""
Move head and tail based on the line.
Return: Unique visited positions.
"""


def move(string, snake):
    visit = []
    if string[0] == "R":
        for x in range(int(string[1])):
            snake[0][1] += 1
            for j in range(9):
                x = follow(snake[j], snake[j + 1])
                visit.append([snake[9][0], snake[9][1]])
                if not x:
                    break
    elif string[0] == "L":
        for x in range(int(string[1])):
            snake[0][1] -= 1
            for j in range(9):
                x = follow(snake[j], snake[j + 1])
                visit.append([snake[9][0], snake[9][1]])
                if not x:
                    break
    elif string[0] == "U":
        for x in range(int(string[1])):
            snake[0][0] -= 1
            for j in range(9):
                x = follow(snake[j], snake[j + 1])
                visit.append([snake[9][0], snake[9][1]])
                if not x:
                    break
    elif string[0] == "D":
        for x in range(int(string[1])):
            snake[0][0] += 1
            for j in range(9):
                x = follow(snake[j], snake[j + 1])
                visit.append([snake[9][0], snake[9][1]])
                if not x:
                    break

    f = [list(t) for t in set(tuple(arr) for arr in visit)]
    f = sorted(f)
    return f


# Initialize required variables
lines = read("input.txt")
rope = []
for i in range(10):
    rope.append([4, 0])
visited = [rope[9]]
lines = [s.replace('\n', '') for s in lines]


"""
Main. 
Return: Total number of coordinates visited by the last rope.
"""

for i in range(len(lines)):
    line = lines[i].split(" ")
    visited += move(line, rope)
k = [list(t) for t in set(tuple(arr) for arr in visited)]
print(len(k))
