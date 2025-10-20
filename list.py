squares = [x**2 for x in range(1, 11)]
print("Squares from 1 to 10:", squares)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print("Even numbers:", evens)
words = ['apple', 'banana', 'cherry']
upper_words = [word.upper() for word in words]
print("Uppercase words:", upper_words)
raw_data = [5, -3, 8, -1, 0, 4]
positives = [x for x in raw_data if x >= 0]
print("Positive numbers:", positives)
tuple_list = [(x, x**2) for x in range(1, 6)]
print("Tuples of (number, square):", tuple_list)
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print("Flattened list:", flattened)
text = "hello world"
vowels = [char for char in text if char in 'aeiou']
print("Vowels in text:", vowels)
base = [1, 2, 3, 4, 5]
times_ten = [x * 10 for x in base]
print("Numbers multiplied by 10:", times_ten)
