def find_common_values(arr1, arr2):
  """11. Write a program to find the common values between two arrays."""
  return list(set(arr1) & set(arr2))
print(find_common_values([1, 2, 3], [2, 3, 4]))