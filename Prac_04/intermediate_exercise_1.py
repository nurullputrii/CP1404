"""
Intermediate Exercises
"""
# Task 1

numbers = []
for user_input in range(1, 5 + 1):
    user_input = int(input('Enter number >>> '))
    numbers.append(user_input)

print(numbers)
print('The first number is {}'.format(numbers[0]))
print('The smallest number is {}'.format(min(numbers)))
print('The largest number is {}'.format(max(numbers)))
average_num = sum(numbers) / 5
print('The average of the numbers is {} '.format(average_num))

