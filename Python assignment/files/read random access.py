# Random access file reading (using 'rb' mode and seek)
with open("example.txt", "rb") as file:
    file.seek(10)  # Move the cursor to byte 10
    content = file.read(5)  # Read 5 bytes from the current position
    print(content)
