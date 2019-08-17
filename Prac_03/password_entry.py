""" This is Nurul's work """

def main():
    MIN_LENGTH = 5
    MAX_LENGTH = 15

    password = get_password()
    print_asterisk(MAX_LENGTH, MIN_LENGTH, password)


def print_asterisk(MAX_LENGTH, MIN_LENGTH, password):
    while len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        print("password less or exceed the desirable length")
        password = get_password()
    print(len(password) * "*")


def get_password():
    password = input("enter password>> ")
    return password


main()