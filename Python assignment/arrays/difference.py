def difference_largest_smallest(arr):
  """ Write a function to get the difference of largest and smallest value."""
  if not arr:
    return 0  # Handle empty array case
  return max(arr) - min(arr)
my_array = [1, 2, 3, 4, 2, 5, 1]
print(difference_largest_smallest(my_array))