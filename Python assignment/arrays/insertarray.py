"""Write a function to insert an element at a specific position in the array."""
def insert_element(arr, element, position):
  new_arr = arr[:]
  new_arr.insert(position, element)
  return new_arr
my_array=[1,3,5,6,7,9]
print(insert_element(my_array, 10, 2))  