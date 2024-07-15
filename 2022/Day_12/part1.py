# Importing needed modules
import collections


"""
Read every line from file.
Return: Array containing all the lines from the file.
"""


def read(filename):
    file = open(filename, "r")
    return file.readlines()


"""
Check if been there.
Return: Boolean
"""


def change(grid, paths, walls):
    for x in paths:
        if grid[x[1]][x[0]] not in walls:
            grid[x[1]][x[0]] = "."


"""
Breadth First Search
Return: Path between start and end.
"""


def bfs(grid, start, goal, wall):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            change(grid, path, walls)
            return path
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x2 < len(grid[0]) and 0 <= y2 < len(grid) and grid[y2][x2] not in wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


# Initialize required variables
lines = read("input.txt")
lines = [s.replace('\n', '') for s in lines]
scores = [[(0, 20)]]
error = 0
counter = 0
distance = 0

"""
Main. 
Return:
"""


for i in range(len(lines)):
    lines[i] = [*lines[i]]


while counter - error < 27:
    walls = ["E"]
    char = chr(97 + counter - error)
    for i in range(ord('a'), ord('z') + 1):
        if not chr(i) == char:
            walls.append(chr(i))
    if counter - error == 26:
        char = "E"
        walls = []
    if chr(97 + counter - error - 1) in walls:
        walls.remove(chr(97 + counter - error - 1))
    try:
        scores.append(bfs(lines, scores[-1][-1], char, walls))
        print(char)
        for i in range(len(lines)):
            changer = ''.join(lines[i])
            print(changer)
        counter += 1
    except IndexError:
        error += 3

asd = 0
for i in scores:
    distance += len(i) - 1
    asd += len(i)
print(distance, asd)
