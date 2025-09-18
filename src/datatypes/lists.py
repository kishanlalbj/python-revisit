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