# Write a program to print the odd and even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers:")
for num in numbers:
  if num % 2 == 0:
    print(num)

print("Odd numbers:")
for num in numbers:
  if num % 2 != 0:
    print(num)