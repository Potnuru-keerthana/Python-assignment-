# Using seek() to adjust the file pointer to a specific index
with open("example.txt", "r") as file:
    file.seek(5)  # Set the pointer to position 5
    content = file.read(10)  # Read the next 10 characters
    print(content)
