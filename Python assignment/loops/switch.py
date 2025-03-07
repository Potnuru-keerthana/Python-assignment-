# Print gender (Male/Female) program according to given M/F using switch
def print_gender(gender):
  if gender.upper() == "M":
    print("Male")
  elif gender.upper() == "F":
    print("Female")
  else:
    print("Invalid gender")

print_gender("m")  # Male
print_gender("F")  # Female
print_gender("X")  # Invalid gender 