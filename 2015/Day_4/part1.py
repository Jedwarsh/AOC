# Import needed modules
import hashlib


"""
Read line from file.
Return: line.
"""


def read(filename):
    file = open(filename, "r")
    return file.readline()


# Initialize required variables
key = read("input.txt")


"""
Main. 
Return: first integer that is if appended to the key string produces an MD5 hash with 5 leading zeros.
"""


for i in range(9999999):
    modified_key = key
    modified_key += str(i)
    m = hashlib.md5(modified_key.encode('UTF-8'))
    if m.hexdigest()[:5] == "00000":
        print(i)
        break
