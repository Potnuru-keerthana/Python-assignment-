""" Write a function to calculate the average value of an array of integers."""
def average_array(arr):
  if not arr:
    return 0  # Handle empty array case
  return sum(arr) / len(arr)
arr=[1,3,5,6,3]
print(average_array(arr))