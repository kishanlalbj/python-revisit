# dicts are similar to objects in js

person = {
    "name": "john",
    "age": 24
}

address = dict(street="Ezhlu Kenaru st", door_no="23/f", city="Poolampatti")

# person.name wont work.
print(person["name"]) 

del address["door_no"]

print('name' in person)
print('door_no' in address)

# person["street"] # 🔴 app crashes when try to access key that doesn't exists 
person.get("street", "No Note") 
person.update(address)


print("==================== Dict")
print(person)

print("==================== .keys()")
print(person.keys())
print(type(person.keys()))

print("==================== .values()")
print(person.values())

print("==================== .items()")
print(person.items())

print("==================== len(dict)")
print(len(person))

# tuple concatenation
print("==================== tuple concatenation")
print(("a", "b") + ("c", "d"))

# Tuple unpacking
print("==================== tuple unpacking")
a, b = ("hello", "world")
print(a)

print(b)

# Tuple to list
print("==================== tuple to list")
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)


# compare tuples
print("==================== compare tuples")
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
print(tuple1 == tuple2)  # True, values are the same
print(tuple1 is tuple2)  # False, different objects in memory
