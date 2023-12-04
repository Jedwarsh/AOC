"""
Read every line from file.
Return: Array containing all the lines from the file.
"""


def read(filename):
    file = open(filename, "r")
    return file.readlines()


"""
Split the string into three parts.
Return: Array containing all three parts.
"""


def split_game(string):
    string = string.replace("\n", "")
    string = string.split("through ")
    end = string[1]
    string[1] = ""
    end = end.split(",")
    string = "".join(string)
    move = string.split(" ")[-3]
    start = string.split(" ")[-2].split(",")
    return [move, start, end]


"""
Count the occurrences of "1" in a 2D array.
Return: Number of occurrences of "1"
"""


def count_lights_in_array(arr):
    count = 0
    for row in arr:
        for element in row:
            if element == 1:
                count += 1
    return count


# Initialize required variables
lines = read("input.txt")
lights = [[0 for col in range(1000)] for row in range(1000)]


"""
Main. 
Return: Number of lit lights.
"""


for line in lines:
    line = split_game(line)
    x_start = line[1][0]
    x_end = line[2][0]
    y_start = line[1][1]
    y_end = line[2][1]
    for i in range(1000):
        for j in range(1000):
            if int(x_start) <= i <= int(x_end) and int(y_start) <= j <= int(y_end):
                if line[0] == "on":
                    lights[i][j] = 1
                if line[0] == "off":
                    lights[i][j] = 0
                if line[0] == "toggle":
                    if lights[i][j] == 1:
                        lights[i][j] = 0
                    else:
                        lights[i][j] = 1
print(count_lights_in_array(lights))
