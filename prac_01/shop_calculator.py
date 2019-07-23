""""if the total price > $100, discount 10%. ask the user the number of items and also the price"""

user_input = int(input("enter number of items: "))
item_list = [float(input("enter the price:$ ")) for i in range(user_input)]
total_item = sum(item_list)
if total_item > 100:
    calculate = total_item - (10/100) * total_item
    print(calculate)
else:
    print("$" + total_item)







