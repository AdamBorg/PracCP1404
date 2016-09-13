"""Adam Borg"""
def main():
    usersName = get_name()

    letter = int(input('What letters would you like to see in your name?'))

    printCharacter(usersName, letter)


def printCharacter(usersName, letter):
    lengthOfName = len(usersName)
    for i in range(letter-1, lengthOfName, letter):
        print(usersName[i])


def get_name():
    usersName = input('What is your name?')
    while usersName == '':
        usersName = input('What is your name?')
    return usersName


main()