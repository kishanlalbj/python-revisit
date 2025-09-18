# set is unique
set_one = set(["test", "test", "test_one", "test_two"]) # {"test", "test", "test_one", ...}

set_two = set(["test", "test_one", "test_three" ])

print(f"Union Sets: {set_one | set_two}")

print(f"Common (intersections): {set_one & set_two}")

print(f"only in set one: f{set_one - set_two}")

print(f"Is test_one in set one ? {'test_one' in set_one}")