# all pyton types are objects just like js

class Person:
    name = ""
    is_adult = True

    def greet(self):
        print(f"Hello, {self.name}")
        return f"Hello, {self.name}"


print(type(Person)) # type 

john = Person()

print(f"john is an adult {john.is_adult}")
john.name = "John Doe"
john.is_adult = False

print(f"john is an adult {john.is_adult}")

john.greet()
print(f"Person is an adult {Person.is_adult}")
print(Person.greet(self=john))