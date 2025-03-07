try:
    with open('some_file.txt', 'r') as file:
        file.read()  # This could raise an IOError if the file doesn't exist or isn't accessible
except IOError as e:
    print(f"IOException: {e}")
