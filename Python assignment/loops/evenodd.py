# Program to check whether a number is EVEN or ODD using switch
def even_or_odd(num):
  if num % 2 == 0:
    return "EVEN"
  else:
    return "ODD"

print(even_or_odd(10))  # EVEN
print(even_or_odd(7))   # ODD