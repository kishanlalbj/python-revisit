# Set is a collection which is unordered, unchangeable*, and unindexed.
# Set is written with curly brackets.
set_one = set(["test", "test", "test_one", "test_two"]) # {"test", "test", "test_one", ...}

set_two = set(["test", "test_one", "test_three", "test-four" ])

print(f"Union Sets: {set_one | set_two}")

print(f"Common (intersections): {set_one & set_two}")

print(f"only in set one: f{set_one - set_two}")

print(f"Is test_one in set one ? {'test_one' in set_one}")

numbers = {1, 2,3,4,5,6}
squared = {n ** 2 for n in numbers}
print(squared)