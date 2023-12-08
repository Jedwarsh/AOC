"""
Read every line from file.
Return: List containing all the lines from the file.
"""


def read(filename):
    file = open(filename, "r")
    return file.readlines()


"""
Convert the cards into values.
Return: List containing values representing the cards.
"""


def convert_hand(string):
    new = []
    for char in string:
        new.append(dictionary[char])
    return new


"""
Convert the type of the hand based on the number of joker in it.
Return: New type of the hand.
"""


def get_new_value_with_joker(value, number_of_jokers):
    if value == 1 and number_of_jokers == 5:
        return 7
    elif value == 1 and number_of_jokers == 4:
        return 7
    elif value == 1 and number_of_jokers == 3:
        return 6
    elif value == 1 and number_of_jokers == 2:
        return 4
    elif value == 1 and number_of_jokers == 1:
        return 2
    elif value == 2 and number_of_jokers == 3:
        return 7
    elif value == 2 and number_of_jokers == 2:
        return 6
    elif value == 2 and number_of_jokers == 1:
        return 4
    elif value == 3 and number_of_jokers == 1:
        return 5
    elif value == 3 and number_of_jokers == 2:
        return 7
    elif value == 4 and number_of_jokers == 1:
        return 6
    elif value == 4 and number_of_jokers == 2:
        return 7
    elif value == 5 and number_of_jokers == 1:
        return 6
    elif value == 5 and number_of_jokers == 2:
        return 7
    elif value == 6 and number_of_jokers == 1:
        return 7
    else:
        return value


"""
Find the type of a hand.
Return: Value representing the type of the hand.
"""


def check_hand(string):
    x = []
    new = convert_hand(string)
    for i in new:
        if i != 1:
            x.append(new.count(i))
    joker = new.count(1)
    if 5 in x:
        value = 7
    elif 4 in x:
        value = 6
    elif 3 in x and 2 in x:
        value = 5
    elif 3 in x:
        value = 4
    elif x.count(2) == 4:
        value = 3
    elif 2 in x:
        value = 2
    else:
        value = 1
    value = get_new_value_with_joker(value, joker)
    new = [value] + new
    return new


# Initialize required variables
result = 0
new_list = []
hands = read("input.txt")
dictionary = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 1,
    "Q": 12,
    "K": 13,
    "A": 14
}


"""
Main. 
Return: Total winnings.
"""


for index_for_hand in range(len(hands)):
    hand = hands[index_for_hand]
    hand = hand.replace("\n", "")
    hand__and_score = hand.split(" ")
    new_list.append([])
    hand = check_hand(hand__and_score[0])
    new_list[index_for_hand].append(hand)
    new_list[index_for_hand].append(hand__and_score[1])
new_list = sorted(new_list)
for index_for_hand in range(len(new_list)):
    result += (index_for_hand+1) * int(new_list[index_for_hand][1])
print(result)
