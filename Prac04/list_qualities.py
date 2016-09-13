def main():
    list = []
    for i in range(0,5):
        number = int(input("Number: "))
        list.append(number)

    print("The first number is {}".format(list[0]))
    print("the last number is {}".format(list[-1]))
    print("The smallest number is", min(list))
    print("The largest number is", max(list))
    print("The average of the numbers is", sum(list) / len(list))

main()