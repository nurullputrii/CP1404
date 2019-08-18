# Task 2

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_input = str(input('Enter the username >>> '))
if user_input not in usernames:
    print("Access denied")
else:
    print('Access granted')

