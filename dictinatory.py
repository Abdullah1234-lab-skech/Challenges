def check_value_frequency(test_dict):
    frequency = {}

    for value in test_dict.values():
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1

    print("Original Dictionary:")
    print(test_dict)
    print("\nValue Frequencies:")
    for val, count in frequency.items():
        print(f"{val}: {count}")
sample_dict = {
    'a': 3,
    'b': 5,
    'c': 3,
    'd': 7,
    'e': 5,
    'f': 3}
check_value_frequency(sample_dict)
