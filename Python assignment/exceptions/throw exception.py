def custom_exception():
    raise Exception("This is a custom exception message")

try:
    custom_exception()
except Exception as e:
    print(f"Exception occurred: {e}")
