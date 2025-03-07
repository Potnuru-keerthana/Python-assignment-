def count_even_odd(arr):
  """ Write a method to find number of even number and odd numbers in an array."""
  even_count = 0
  odd_count = 0
  for num in arr:
    if num % 2 == 0:
      even_count += 1
    else:
      odd_count += 1
  return even_count, odd_count
my_array=[2,4,3,1,5,6,7,9,10]
print(count_even_odd(my_array)) 