# Example 1: Unpacking arguments
def print_numbers(a, b, c):
    print(f"a={a}, b={b}, c={c}")

numbers = [1, 2, 3]
print_numbers(*numbers)  # Output: a=1, b=2, c=3

# Example 2: Unpacking a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
name, age, city = person.values()  # Error: Too many values to unpack
# name, age, city = (*person.values(),)  # Unpacking the dictionary values
print(name, age, city)  # Output: Alice 25 New York

# Example 3: Unpacking a list/tuple in another list/tuple
numbers = [1, 2, 3]
new_list = [0, *numbers, 4, 5]
print(new_list)  # Output: [0, 1, 2, 3, 4, 5]

# Example 4: Multiplying a sequence
print([0] * 5)  # Output: [0, 0, 0, 0, 0]
