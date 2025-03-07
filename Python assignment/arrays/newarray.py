def remove_duplicates_return_new(arr):
  """ Write a program to remove the duplicate elements and return the new array."""
  return list(set(arr))
my_array = [1, 2, 3, 4, 2, 5, 1]
print(remove_duplicates_return_new(my_array))  