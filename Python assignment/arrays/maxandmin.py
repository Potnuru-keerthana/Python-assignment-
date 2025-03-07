""" Write a function to find the minimum and maximum value of an array."""
def min_max_array(arr):
  if not arr:
    return None, None  # Handle empty array case
  return min(arr), max(arr)
my_array=[1,2,3,5,6,7,8,9]
print(min_max_array(my_array)) 
