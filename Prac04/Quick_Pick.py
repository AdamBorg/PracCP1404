import random

def main():
    #Get number from user
    Number_Of_Quickpicks = int(input("How many quick picks would you like? "))

    #Run quickpick calculator for as many quickpicks as they would like
    for i in range(Number_Of_Quickpicks):

        #Intiate lists
        numbers_list = []
        used_numbers = []

        #Assign numbers to list and check that they are not repeated
        while len(numbers_list) <6:
            random_number = random.randint(1,45)
            if random_number not in used_numbers:
                used_numbers.append(random_number)
                numbers_list.append(random_number)

        #print list to the user
        print(" ".join(str(x) for x in sorted(numbers_list)))


main()