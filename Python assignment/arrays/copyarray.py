"""6. Write a function to copy an array to another array."""
def copy_array(arr):
  return arr[:]  # Create a shallow copy 
my_array=[1,3,6,2,7,8,9,10]
print(copy_array(my_array))  # [1, 2, 3, 4, 2, 5, 1]