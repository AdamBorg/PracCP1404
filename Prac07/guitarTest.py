from Prac07.guitar import Guitar


def main():
    guitars = []
    menu(guitars)

    for product in guitars:
        print(product)


def menu(guitars):
    quickBool = False
    while quickBool == False:
        guitar_name = input("Guitar Name: ")
        if guitar_name == "".strip():
            break
        guitar_year = input("Year Made: ")
        guitar_price = input("Price: ")
        guitars.append(Guitar(guitar_name, guitar_year, guitar_price))
    return guitars
main()