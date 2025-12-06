from math import pow


# similar to js doc we can document the func like this
def greet(name):
    """
    Greets the given name
    
    :param name: name of the person

    :return: Hello :param name
   """
    return f"Hello, {name}"

print(greet("john"))


def calculateBMI(height, weight):
    return weight /  pow(height, 2)

print(f"my bmi is {calculateBMI(weight=84.5, height=1.72)}")

name = "Jane"
lang = "fr"

def greet_de(name):
    if lang == "fr": return f"Bounjour, {name}"
    else: return f"Hello, {name}"

print(greet_de("John"))


def multiply(*args, **kwargs):
    print("args", *args)
    print("extras", kwargs)
    result = 1
    for n in args:
        result *= n

    return result

print(multiply(1,2,3,4, name="multiply"))

dict = {"name": "kishan"}

def greet_dict(obj):
    obj["name"] = "Hacked"
    print(obj)


greet_dict(dict)


def calculateTotal(items=[]):
    items.append(2)
    result = 0
    for i in items:
        result += i
    print(result)

calculateTotal() # 2
calculateTotal() # 4

def calculateTotalNew(items=None):
    if items is None:
        items = []
    result = 0
    for i in items:
        result += i

    print(result)

calculateTotalNew()


def isEven(num):
    """Returns if a num is even or not"""
    return True if num % 2 == 0 else False

print(isEven.__doc__)
print(isEven.__name__)
