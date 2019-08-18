"""
WARM UP SECTION
numbers = [3, 1, 4, 1, 5, 9, 2]
1. numbers[0] = 3
2. numbers[-1] = 2
3. numbers[3] = 1
4. numbers[ : -1] = [3, 1, 4, 1, 5, 9]
5. numbers[3:4] = [1]
6. 5 in numbers = True
7. 7 in numbers = False
8. 3 in numbers = False
9. numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""

numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers)
# Change the first element of numbers to “ten”
numbers[0] = 'ten'
print(numbers)
# # # Change the last element of numbers to 1
numbers[-1] = 1
print(numbers)
# Get all the elements from numbers except the first two
del(numbers[:2])
print(numbers)
# Check if 9 is an element of numbers
check = 9 in numbers
if check is True:
    print("9 is an element of numbers")
else:
    print('9 is not in the element of numbers')
