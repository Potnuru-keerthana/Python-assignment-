def second_largest(arr):
  """13 & 14. Write a method to find the second largest number in an array."""
  if len(arr) < 2:
    return None  # Not enough elements
  unique_sorted = sorted(list(set(arr)), reverse=True)
  if len(unique_sorted) < 2:
    return None  # No second largest if all elements are the same
  return unique_sorted[1]
my_array = [1, 2, 3, 4, 2, 5, 1]
print(second_largest(my_array)) 