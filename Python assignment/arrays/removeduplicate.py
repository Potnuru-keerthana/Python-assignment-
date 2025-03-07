"""5. Write a function to remove a specific element from an array."""
def remove_element(arr, element):
  new_arr = arr[:]  # Create a copy to avoid modifying the original
  try:
    new_arr.remove(element)
    return new_arr
  except ValueError:
    return arr  # Element not found, return original array
my_array=[1,2,3,4,5,6]
print(remove_element(my_array, 2))