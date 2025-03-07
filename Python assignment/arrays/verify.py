def contains_elements(arr, elem1, elem2):
  """ Write a method to verify if the array contains two specified elements """
  return elem1 in arr and elem2 in arr
my_array = [1, 2, 3, 4, 2, 5, 1]
print(contains_elements(my_array, 2, 5))
