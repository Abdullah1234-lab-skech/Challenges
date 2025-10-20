set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
symmetric_diff_set = set1.symmetric_difference(set2)
list1 = list(set1)
list2 = list(set2)
symmetric_diff_list = [item for item in list1 + list2 if item not in set1.intersection(set2)]
print("Set 1:", set1)
print("Set 2:", set2)
print("\nSymmetric Difference (using sets):", symmetric_diff_set)
print("Symmetric Difference (using arrays):", symmetric_diff_list)
