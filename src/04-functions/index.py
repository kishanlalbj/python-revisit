from math import pow

# Import pow from the math module so we can calculate powers like height squared.

# A simple function with one parameter.
def greet(name):
    """
    Greets the given name.

    :param name: name of the person
    :return: A greeting string containing the name.
    """
    return f"Hello, {name}"

print(greet("john"))


# A function with positional parameters that calculates Body Mass Index.
def calculateBMI(height, weight):
    # Use pow(height, 2) to square the height.
    return weight / pow(height, 2)

# Demonstrates calling a function with keyword arguments.
print(f"my bmi is {calculateBMI(weight=84.5, height=1.72)}")

name = "Jane"
lang = "fr"

# Use a global variable to choose the greeting language.
def greet_de(name):
    if lang == "fr":
        return f"Bounjour, {name}"
    else:
        return f"Hello, {name}"

print(greet_de("John"))


# `*args` collects extra positional arguments.
# `**kwargs` collects extra keyword arguments.
def multiply(*args, **kwargs):
    print("args", *args)
    print("extras", kwargs)
    result = 1
    for n in args:
        result *= n

    return result

print(multiply(1, 2, 3, 4, name="multiply"))

# Use a descriptive variable name instead of the built-in `dict`.
person_dict = {"name": "kishan"}

# A function can mutate a mutable object like a dictionary.
def greet_dict(obj):
    obj["name"] = "Hacked"
    print(obj)


greet_dict(person_dict)


def calculateTotal(items=[]):
    # The default list is created once when the function is defined.
    # Each call reuses the same list, which can cause unexpected behavior.
    items.append(2)
    result = 0
    for i in items:
        result += i
    print(result)

calculateTotal()  # 2
calculateTotal()  # 4  (the same list is reused across calls)


def calculateTotalNew(items=None):
    # Use None as the default value to avoid shared mutable state.
    if items is None:
        items = []
    result = 0
    for i in items:
        result += i

    print(result)

calculateTotalNew()  # 0


def isEven(num):
    """Returns whether a number is even."""
    return True if num % 2 == 0 else False

print(isEven.__doc__)
print(isEven.__name__)
