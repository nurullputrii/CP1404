"""
count a how many a string in a text
"""

my_dict = {}
user_input = str(input('Enter a text >>> '))
words = user_input.split(" ")

for word in words:
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1

for key, value in my_dict.items():
    print('{}: {}'.format(key, value))






