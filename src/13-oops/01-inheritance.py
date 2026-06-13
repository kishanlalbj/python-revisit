
# Single Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"name is {self.name} and age is {self.age}")



class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age) # call the parent constructor
        self.emp_id = emp_id

    def display_employee(self):
        print(f"name is {self.name}. age is {self.age}")



print("="*20)
print("Multi Level Inheritance")
print("="*20)
class Father1:
    def father_quality(self):
        print("father quantity")

class Son1(Father1):
    def son_quality(self):
        print("son quality")

class GrandSon(Son1):
    def grandson_quality(self):
        print("grandson quality")

multilevel_child = GrandSon()

multilevel_child.father_quality()
multilevel_child.son_quality()
multilevel_child.grandson_quality()


# Multiple Inheritance
print("="*20)
print("Multiple Inheritance")
print("="*20)

class Father:
    def father_quality(self):
        print("father quality")

class Mother:
    def mother_quality(self):
        print("mother quality")

class Son(Father, Mother):
    def son_quality(self):
        print("Son  Quality")

son = Son()

son.father_quality()
son.mother_quality()
son.son_quality()