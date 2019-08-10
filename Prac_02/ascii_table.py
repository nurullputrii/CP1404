LOWER_NUM = 33
UPPER_NUM = 127

user_input_char = str(input("enter a character: "))
switch_char_to_num = ord(user_input_char)
print(switch_char_to_num)

user_input_num = int(input("enter a number between 33 and 127: "))

while LOWER_NUM >= user_input_num <= UPPER_NUM:
    print("number must be between ", LOWER_NUM, " and ", UPPER_NUM)
    user_input_num = int(input("enter a number between 33 and 127: "))

switch_num_to_char = chr(user_input_num)
print(switch_num_to_char)
