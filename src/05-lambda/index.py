# Lambdas are anonymous (one-line) functions in Python.
add_one = lambda x: x + 1

# Use the returned value from add_one.
print(add_one(10))
print(add_one(4))

numbers = [1, 34, 45, 67, 44, 45, 68]

# filter() returns an iterator of items where the lambda returns True.
# We wrap it with list() so we can print all values at once.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# JavaScript equivalent for comparison:
# const even = numbers.filter((x) => x % 2 == 0)