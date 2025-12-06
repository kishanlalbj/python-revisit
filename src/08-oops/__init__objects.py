class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    name = ""
    age = -1

    def greet(self):
        return f"Hell, ${self.name}"
    
    def is_adult(self) -> bool:
        return True if self.age >= 18 else False
    


john = Person("John", 18)

print(john.greet())
print(john.is_adult())

jane = Person("Jane", 15)
# jane.age = 21
print(jane.is_adult())