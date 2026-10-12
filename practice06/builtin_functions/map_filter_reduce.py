from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() - multiply every number by 2
doubled_numbers = list(map(lambda x: x * 2, numbers))

print("Original numbers:", numbers)
print("Doubled numbers:", doubled_numbers)

# filter() - get only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Another example with strings
names = ["Alice", "Bob", "Alexander", "John", "Anna"]

# Convert every name to uppercase
uppercase_names = list(map(str.upper, names))

print("Original names:", names)
print("Uppercase names:", uppercase_names)


# Get names with more than 4 characters
long_names = list(filter(lambda name: len(name) > 4, names))

print("Names longer than 4 characters:", long_names)

numbers = [1, 2, 3, 4, 5]

# Calculate the sum of all numbers
total = reduce(lambda x, y: x + y, numbers)

print("Numbers:", numbers)
print("Sum:", total)


# Calculate the product of all numbers
product = reduce(lambda x, y: x * y, numbers)

print("Product:", product)

names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]


# enumerate()
print("\nUsing enumerate():")

for index, name in enumerate(names):
    print(index, name)


# enumerate() starting from 1
print("\nNumbered names:")

for index, name in enumerate(names, start=1):
    print(index, name)


# zip()
print("\nUsing zip():")

for name, score in zip(names, scores):
    print(name, score)


# Convert zip() result into a list
students = list(zip(names, scores))

print("\nStudents:", students)