"""
Read every line from file.
Return: Array containing all the lines from the file.
"""


def read(filename):
    file = open(filename, "r")
    return file.readlines()


"""
Move head and tail based on the line.
Return: Unique visited positions.
"""


def move(string, start, end):
    visit = []

    if string[0] == "R":
        for x in range(int(string[1])):
            abs_x = abs(start[0] - end[0])
            abs_y = abs(start[1] + 1 - end[1])
            if start == end or 0 <= abs_x < 2 and 0 <= abs_y < 2:
                start[1] += 1
            else:
                if start[0] != end[0] and start[1] != end[1]:
                    end[0] = start[0]
                    end[1] = start[1]
                    start[1] += 1
                else:
                    start[1] += 1
                    end[1] += 1
                visit.append([end[0], end[1]])

    elif string[0] == "L":
        for x in range(int(string[1])):
            abs_x = abs(start[0] - end[0])
            abs_y = abs(start[1] - 1 - end[1])
            if start == end or 0 <= abs_x < 2 and 0 <= abs_y < 2:
                start[1] -= 1
            else:
                if start[0] != end[0] and start[1] != end[1]:
                    end[0] = start[0]
                    end[1] = start[1]
                    start[1] -= 1
                else:
                    start[1] -= 1
                    end[1] -= 1
                visit.append([end[0], end[1]])

    elif string[0] == "U":
        for x in range(int(string[1])):
            abs_x = abs(start[0] - 1 - end[0])
            abs_y = abs(start[1] - end[1])
            if start == end or 0 <= abs_x < 2 and 0 <= abs_y < 2:
                start[0] -= 1
            else:
                if start[0] != end[0] and start[1] != end[1]:
                    end[0] = start[0]
                    end[1] = start[1]
                    start[0] -= 1
                else:
                    start[0] -= 1
                    end[0] -= 1
                visit.append([end[0], end[1]])

    elif string[0] == "D":
        for x in range(int(string[1])):
            abs_x = abs(start[0] + 1 - end[0])
            abs_y = abs(start[1] - end[1])
            if start == end or 0 <= abs_x < 2 and 0 <= abs_y < 2:
                start[0] += 1
            else:
                if start[0] != end[0] and start[1] != end[1]:
                    end[0] = start[0]
                    end[1] = start[1]
                    start[0] += 1
                else:
                    start[0] += 1
                    end[0] += 1
                visit.append([end[0], end[1]])

    f = [list(t) for t in set(tuple(arr) for arr in visit)]
    f = sorted(f)
    return f


# Initialize required variables
lines = read("input.txt")
head = [4, 0]
tail = [4, 0]
visited = [[tail[0], tail[1]]]
lines = [s.replace('\n', '') for s in lines]


"""
Main. 
Return: Total number of coordinates visited by the tail rope.
"""

for i in range(len(lines)):
    line = lines[i].split(" ")
    visited += move(line, head, tail)
k = [list(t) for t in set(tuple(arr) for arr in visited)]
print(len(k))
