def main():
    lower = 33
    upper = 127

    num_entered = get_number(lower,upper)

    print("{:>3} {:>6} \n".format(num_entered, chr(num_entered)))

    print_ascii_table(lower, upper)

def get_number(lower,upper):
    num_entered = 0
    exit_character = 'e'

    while num_entered < 33 or num_entered > 127 or exit_character == 'e':
        try:
            num_entered = int(input("please enter a number between {} and {} \n".format(lower, upper)))
            exit_character = 'i'

        except ValueError:
            print("Please enter a valid number")


    return num_entered

def print_ascii_table(lower, upper):
    for i in range(lower, upper):
        print("{:>3} {:>6}".format(i, chr(i)))

main()

#made change to see what happens when pushed to gitHub