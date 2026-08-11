nested_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for sublist in nested_lists:
    sublist.clear()
print(f"Nested lists after clear: {nested_lists}")