# Matching a String Against a Regular Expression With match()
import re
pattern = r"H\w+"  # Matches words starting with "H"
string = "Helloworld"
match = re.match(pattern, string)
if match:
    print("Match found:", match.group())  # Output: Match found: Hello
else:
    print("No match found")
