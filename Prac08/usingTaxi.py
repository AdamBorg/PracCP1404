from Prac08.taxi import Car
from Prac08.taxi import Taxi
from Prac08.taxi import UnreliableCar
from Prac08.taxi import SilverServiceTaxi

def main():
   # taxi = Taxi("Prius 1", 100)
   # taxi.drive(40)
   # print(taxi)
   # print("Current fare: {}".format(taxi.get_fare()))

   # taxi.start_fare()
   # taxi.drive(100)
   # print(taxi)
   # print("Current fare: {}".format(taxi.get_fare()))

   # unreliable_vehicle = UnreliableCar("Datsun", 100, 20)
   # unreliable_vehicle.drive(40)
   # print

    car = SilverServiceTaxi("Hummer",200, 2)
    car.drive(10)
    print(car)
    print("Current fare: {}".format(car.get_fare()))

main()