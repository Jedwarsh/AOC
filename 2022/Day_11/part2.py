"""
Read every line from file.
Return: Array containing all the lines from the file.
"""


def read(filename):
    file = open(filename, "r")
    return file.readlines()


"""
Monkey class
"""


class Monkey:
    def __init__(self, items, operator, num2, divisor, true, false):
        self.items = items
        self.true = true
        self.false = false
        self.operator = operator
        self.num2 = num2
        self.divisor = divisor
        self.inspect = 0

    """
    Method for the monkey object to count the worry level.
    Return: New worry level.
    """

    def operation(self, num):
        if self.num2 == "X":
            if self.operator == '+':
                num = num + num
            elif self.operator == '*':
                num = num * num
            self.inspect += 1
            return num
        if self.operator == '+':
            num = num + self.num2
        elif self.operator == '*':
            num = num * self.num2
        elif self.operator == '-':
            num = num - self.num2
        elif self.operator == '/':
            num = num / self.num2

        self.inspect += 1
        return num

    """
    Method for the monkey class that decides where does the monkey throws the item.
    Return: Next monkey.
    """

    def test(self, num):
        if num % self.divisor == 0:
            return self.true
        else:
            return self.false


# Initialize required variables
lines = read("input.txt")
lines = [s.replace('\n', '') for s in lines]
i = 0
monkey = []
modulo = 1


"""
Main. 
Return: Level of monkey business after 10000 rounds of stuff-slinging simian shenanigans
"""


for line_num in range(len(lines)):

    if len(lines[line_num]) > 0 and lines[line_num][0] == "M":

        x_items = lines[line_num + 1][18:].split(", ")
        x_items = [int(integer) for integer in x_items]

        oper = lines[line_num + 2].split(" ")
        if oper[-1] == "old":
            oper_num = "X"
        else:
            oper_num = int(oper[-1])
        modulo *= int(lines[line_num + 3].split(" ")[-1])
        monkey.append(Monkey(x_items, oper[-2],
                             oper_num,
                             int(lines[line_num + 3].split(" ")[-1]),
                             int(lines[line_num + 4].split(" ")[-1]),
                             int(lines[line_num + 5].split(" ")[-1])))
    i += 1
for loop in range(10000):
    for mon in monkey:
        while len(mon.items) > 0:
            item = mon.items[0]
            ans = mon.operation(item)
            if ans > modulo:
                ans %= modulo
            mon.items.pop(0)
            goal = mon.test(ans)
            monkey[goal].items.append(ans)
monkey.sort(key=lambda x: x.inspect, reverse=True)
print(monkey[0].inspect * monkey[1].inspect)

