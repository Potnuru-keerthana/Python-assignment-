"""3. Write a program to find the index of an array element."""
def find_index(arr, element):
  try:
    return arr.index(element)
  except ValueError:
    return -1  # Element not found
my_array=[1,2,3,4,5,6]
print(find_index(my_array, 3))  # 2