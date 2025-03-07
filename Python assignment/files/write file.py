# Writing to a text file using InputStream (stdin as input stream)
with open("output.txt", "w") as file:
    user_input = input("Enter some text to write to file: ")
    file.write(user_input)
