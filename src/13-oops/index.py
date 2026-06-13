# parameterized construnctor
class Person:

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name is {self.name}, age is {self.age}")


# no-arg constructor
class Empployee:
    def __init__(self):
        self.name = "john"


