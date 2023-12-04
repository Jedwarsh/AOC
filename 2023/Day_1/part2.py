file1 = open('input.txt', 'r')
lines = file1.readlines()
counter = 0
digits = []
numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
for line in lines:
    for i in range(len(line)):
        k = 6 if i+6 <= len(line) else len(line)-i
        for j in range(3, k):
            sub_line = line[i:i+j]
            temp = sub_line
            for key, value in numbers.items():
                if key in sub_line:
                    sub_line = sub_line.replace(key, value+key[-1])
                    line = line.replace(temp, sub_line)

    digits = [int(i) for i in line if i.isdigit()]
    first_and_last = [digits[0], digits[-1]]
    counter += 10*first_and_last[0] + first_and_last[1]

print(counter)