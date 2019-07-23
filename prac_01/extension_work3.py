
user_name = str(input("enter your name: "))
user_choice = ""

valid_inputs = ["H", "G", "Q"];
while user_choice != 'Q':
    print("(H)ello\n"
          "(G)oodbye\n"
          "(Q)uit")
    user_choice = str(input("enter your choice: "))
    user_choice = user_choice.upper()
    if user_choice == "H":
        print("Hello " + user_name)
    elif user_choice == "G":
        print("Goodbye " + user_name)
    elif user_choice == "Q":
        print("Finished")
    else:
        print("Invalid choice")







