# TASK 1
# loops odd number between 1 and 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100
for i in range (0, 101, 10):
    print(i, end=" ")
print()
# count down loop from 20 to 1
countdown = 20
for i in reversed(range(1, countdown+1)):
    print(i, end=" ")
print()

# TASK 2
# print many starts based on the user input
# user_input = int(input("enter number of stars: "))
# star_list= ['*' for i in range(user_input)]
#
# print(' '.join(['%s' % i for i in star_list]))
user_input = int(input("enter number of stars: "))
for i in range (1, user_input+1):
    print("*", end=" ")
print()

# increasing stars per line
user_input = int(input("enter number of stars: "))
for i in range (0, user_input+1):
    for j in range(0, i):
        print("*", end=" ")
    print()

# TASK 3
# Add a loop to the sales bonus exercise you did above, so that the program repeatedly asks for the user's sales and prints the bonus until they enter a negative number.
# Remember that until is the opposite of while.
sales = 1
while sales > 0:
    sales = float(input("Enter sales: $"))
    if 0 < sales < 1000:
        calculate = (10/100)*sales
        print(calculate)
    elif sales >= 1000:
        calculate = (15/100)*sales
        print(calculate)
    else:
        print("Invalid input")
        exit()