"""x and y are the only inputs that the user enters once the programs starts running
the following choices are: 1) showing the even numbers from x to y. 2) show the odd numbers from x to y. 3)show the squares from x to y. 4) exit the program """

user_input = [int(input("enter the number: ")) for i in range(2)]

even_list = []
for number in range(user_input[0], user_input[1]+1):
    if number % 2 == 0:
        even_list.append(number)
print("even number: ", even_list)

odd_list = []
for number in range(user_input[0], user_input[1]+1):
    if number % 2 == 1:
        odd_list.append(number)
print("odd number: ", odd_list)

square_list = []
for number in range(user_input[0], user_input[1]+1):
    square_list.append(number ** 2)
print("the square number: ", square_list)






