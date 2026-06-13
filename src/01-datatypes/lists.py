# lists are ordered, changeable, and allow duplicate values.
# Lists are written with square brackets.

fruits = ["apple", "banana", "cherry", "date", "apple"]
list1 = ["abc", 34, True, 40, "male"]

print(fruits)

print(len(fruits))
print(type(fruits)) # <class 'list'>

#constructor 
new_list = list(("apple", "banana", "cherry"))
print(new_list)

if "apple" in fruits:
    print("Yes, 'apple' is in the fruits list")


fruits.append("orange")
fruits.insert(1, "kiwi")
fruits.remove("banana")
fruits.pop()  # removes the last item
fruits.pop(1)  # removes the item at index 1
fruits.sort()  # sorts the list in ascending order
# fruits.clear()  # removes all items
fruits.reverse()

veggies = ["carrot", "cabbage", "brinjal"]

mix_veg_fruits = fruits + veggies

print(mix_veg_fruits)


# Accessing list items
print(fruits[0])  # first item
print(fruits[-1])  # last item
print(fruits[1:4])  # items from index 1 to 3


# extend
print("Extending fruits with veggies:")
fruits.extend(veggies)
print(fruits)

# list comprehension
squared_numbers = [x**2 for x in range(10)]
print(squared_numbers)


[fruit for fruit in fruits if "apple" == fruit]  # list of fruits containing "apple"

copy_fruits = fruits.copy()  # creates a copy of the fruits list
print(copy_fruits)

print(f'same object in memory: {fruits is copy_fruits}')  # False, different objects
