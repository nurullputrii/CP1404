def name():
    file = open('name.txt', 'w')
    file.write(input("enter your name: "))  # task 1
    file.close()

    file = open('name.txt', 'r') # task 2
    for i in file:
        print("your name is", i)
name()

def number():
    file = open('numbers.txt', 'r')
    calculate = int(file.readline()) + int(file.readline(2))  # task 3
    print(calculate)

number()

file = open('numbers.txt', 'r')  # task 4

total = 0
for line_str in file:
    line_str = line_str.strip()
    num = int(line_str)
    total += num
print(total)
