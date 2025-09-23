
# lambdas are anonymous functions in python
add_one = lambda x: x + 1

add_one(10)

print(add_one(4))


numbers = [1 ,34, 45,67, 44, 45,68]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)

# const even = numbers.filter((x) => x % 2 == 0)