# dicts are similar to objects in js

person = {
    "name": "john",
    "age": 24
}

address = dict(street="Kenaru st", door_no="23/f", city="Poolampatti")

# person.name wont work.
print(person["name"]) 

del address["door_no"]

print('name' in person)
print('door_no' in address)

# person["street"] # 🔴 app crashes when try to access key that doesn't exists 
person.get("street", "No Note") 
person.update(address)

print(person)

print(person.keys())
print(person.values())
print(person.items())
print(len(person))