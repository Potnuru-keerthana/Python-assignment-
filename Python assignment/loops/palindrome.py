# Write a program to palindrome or not.
def is_palindrome(text):
  text = str(text).lower()
  return text == text[::-1]

print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False