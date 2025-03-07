# Write a program to find Armstrong number or not
def is_armstrong(num):
  num_str = str(num)
  n = len(num_str)
  sum = 0
  for digit in num_str:
    sum += int(digit) ** n
  return sum == num

print(is_armstrong(153))  # True
print(is_armstrong(123))  # False