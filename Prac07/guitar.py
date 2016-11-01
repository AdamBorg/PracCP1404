class Guitar:
    def __init__(self, name ="", year = 0 ,cost = 0):
        self.cost = cost
        self.name = name
        self.year = year

    def __str__(self):
        return "Guitar : {:>20} ({}), worth ${:10,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        self.age = 2016 - self.year
        print("The {} is {} years old".format(self.name,self.age))
        return self.age

    def is_vintage(self):
        if self.age >= 50:
            self.vintage_string = "(Vintage)"

        else:
            self.vintage_string = ""