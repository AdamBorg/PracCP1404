def main():
    in_char = input("please enter a character")

    print("The ASCII code for {} is {} ".format(in_char, ord(in_char)))




    num_entered = get_number(lower,upper)

    for num_entered in range(lower, upper):
        print("{:>3} {:>6}".format(num_entered, chr(num_entered)))


def get_number(lower,upper):

    try:
        num_entered = int(input("please enter a number between {} and {}".format(lower, upper)))

    except ValueError:
        print("Please enter a valid number")

    return num_entered

main()
