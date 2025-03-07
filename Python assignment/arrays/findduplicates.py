def find_duplicates(arr):
  """Write a function to find the duplicate values of an array."""
  duplicates = []
  seen = set()
  for item in arr:
    if item in seen and item not in duplicates:
      duplicates.append(item)
    seen.add(item)
  return duplicates
my_array = [1, 2, 3, 4, 2, 5, 1]
print(find_duplicates(my_array))  