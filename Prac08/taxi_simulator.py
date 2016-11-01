from Prac08.taxi import Taxi
from Prac08.taxi import SilverServiceTaxi

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0

    print("Let's Drive")
    print("q)uit, c)hoose taxi, d)rive")

    user_input = input(">>> ").lower()

    while user_input != "q":
        if user_input == 'c':
            print("Taxis available:")
            for i in range(0, len(taxis)):
                print("{} - {}".format(i, taxis[i]))

            taxi_chossen = int(input("Choose taxi: "))
            taxi = taxis[taxi_chossen]

            print("Bill to date: ${:.2f}".format(bill))
            bill = taxis[0].get_fare() + (taxis[1].get_fare() + taxis[2].get_fare()) - 9


            print("q)uit, c)hoose taxi, d)rive")
            user_input = input(">>> ").lower()

        elif user_input == "d":

            distance = int(input("Drive how far? "))
            taxi.drive(distance)

            bill = taxis[0].get_fare() + (taxis[1].get_fare() + taxis[2].get_fare()) - 9
            print("Your {} cost you ${:.2f}".format( 'Prius ',taxis[taxi_chossen].get_fare()))
            print("Bill to date: ${:.2f}".format(bill))


            print("q)uit, c)hoose taxi, d)rive")
            user_input = input(">>> ").lower()


main()