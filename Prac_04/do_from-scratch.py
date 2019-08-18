"""
Display lines (based on the user input) that contains 6 numbers
Each of the 6 numbers has to be from 1-45
Print in ascending order. And no repeated numbers

"""

import random

MIN_VALUE = 1
MAX_VALUE = 45

user_input = int(input('How many quick picks >>> '))



for quick_picks in range(user_input):
    numbers = []


    for num in range(0, 6):
        while True:
            num1 = random.randrange(1, 45)
            if num1 not in numbers:
                numbers.append(num1)
                break

    print(numbers)

