class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.typing = typing
        self.reflection = reflection
        self.name = name
        self.year = year

    def __str__(self):
        return "{}, {}, Reflection = {}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                      self.year)

    def is_dynamic(self):
        if self.typing == "Dynamic":
            print("True")
        else:
            print("False")