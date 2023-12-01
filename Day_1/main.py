file1 = open('Day_1/myfile.txt', 'r')
lines = file1.readlines()
counter = 0

for line in lines:
    digits = [int(i) for i in line if i.isdigit()]
    first_and_last = [digits[0], digits[-1]]
    counter = counter + 10*first_and_last[0] + first_and_last[1]
print(counter)