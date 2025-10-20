
def square_it_out(start, end):
    squared_numbers = [num ** 2 for num in range(start, end + 1)]
    even_squares = [sq for sq in squared_numbers if sq % 2 == 0]
    odd_squares = [sq for sq in squared_numbers if sq % 2 != 0]

    print(f"\nSquared numbers from {start} to {end}:")
    print(squared_numbers)
    print("\nEven squared values:")
    print(even_squares)
    print("\nOdd squared values:")
    print(odd_squares)
try:
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))

    if start_range > end_range:
        print("Start of range must be less than or equal to end of range.")
    else:
        square_it_out(start_range, end_range)
except ValueError:
    print("Please enter valid integers.")
