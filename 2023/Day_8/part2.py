# Importing needed modules
from math import gcd


"""
Read every line from file.
Return: Array containing all the lines from the file.
"""


def read(filename):
    file = open(filename, "r")
    return file.readlines()


"""
Remove specific characters from list of strings.
Return: New list containing only the nodes from the original strings.
"""


def remove_characters(strings):
    for index in range(len(strings)):
        strings[index] = strings[index].replace("\n", "")
        strings[index] = strings[index].replace("= ", "")
        strings[index] = strings[index].replace(",", "")
        strings[index] = strings[index].replace("(", "")
        strings[index] = strings[index].replace(")", "")
        strings[index] = strings[index].split(" ")
    return strings


"""
Find LCM.
Return: LCM.
"""


def get_lcm(numbers):
    lcm = 1
    for i in numbers:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


"""
Find new node
Return: Index of the new node.
"""


def return_new_node(strings, node):
    new_index = 0
    for index in range(len(strings)):
        if strings[index][0] == node:
            new_index = index
    return new_index


# Initialize required variables
all_steps = []
current_move = 0
lines = read("input.txt")
lines = remove_characters(lines)
moves = lines[0][0]
nodes = lines[2:]
nodes = sorted(nodes)


"""
Main. 
Return: Number of steps required to reach end node.
"""


for i in range(len(nodes)):
    if nodes[i][0][2] != "A":
        continue
    current_node_id = i
    steps = 0
    while True:
        if moves[current_move] == "R":
            current_node = nodes[current_node_id][2]
        else:
            current_node = nodes[current_node_id][1]
        steps += 1
        if current_node[2] == "Z":
            all_steps.append(steps)
            current_move = 0
            break
        current_node_id = return_new_node(nodes, current_node)
        if current_move + 1 == len(moves):
            current_move = 0
        else:
            current_move += 1
print(get_lcm(all_steps))
