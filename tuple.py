def process_tuple(numbers):
    total_sum = sum(numbers)
    total_product = 1
    for num in numbers:
        total_product *= num
    print("Original Tuple:", numbers)
    print("Sum of all numbers:", total_sum)
    print("Product of all numbers:", total_product)
my_tuple = (2, 4, 6, 8)
process_tuple(my_tuple)
