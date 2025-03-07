# Reading a file stream (binary mode for streams)
with open("example.txt", "rb") as file:
    content = file.read()
    print(content)
