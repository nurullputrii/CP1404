"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
answer: the ValueError occur when the user input is not integer
2. When will a ZeroDivisionError occur?
answer : ZeroDivisionError occur when the user put 0 in denominator section
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
answer : the code below
"""


finished = False
while not finished:
    try:
        numerator = int(input("Enter the numerator: "))

        denominator = 0
        while denominator == 0:
            denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)


    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished")