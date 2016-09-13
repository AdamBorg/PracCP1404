def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
    'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
    'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    users_username = str(input("Your username please: "))

    if users_username in usernames:
        print("Access Granted")
    else:
        print("Access Denied")


main()