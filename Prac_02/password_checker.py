"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|"

def main():
    print("Please enter a valid password\n"
          "Your password must be between 5 and 15 characters, and contain:\n"
          "\t 1 or more uppercase characters\n"
          "\t 1 or more lowercase characters\n"
          "\t 1 or more numbers\n"
          "\t and 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("enter password: ")
    if valid_input(password):
        print("Your {}-character password is valid: {}".format(len(password), password))
    else:
        print('Password not valid')



def valid_input(password):
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    for i in password:
        if i >= 'A' and i <= 'Z':
            count_upper += 1
        elif i >= 'a' and i <= 'z':
            count_lower += 1
        elif i in SPECIAL_CHARACTERS:
            count_special += 1
        elif i.isdigit() == True:
            count_digit += 1

    if count_upper >= 1 and count_lower >=1 and count_digit >= 1 and count_special >=1:
        return True
    else:
        return False
main()