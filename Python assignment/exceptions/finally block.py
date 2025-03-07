try:
    x = 10
    y = 0
    result = x / y  # This will raise an exception
except ZeroDivisionError as e:
    print(f"Caught error: {e}")
finally:
    print("This will always be executed, regardless of an exception")
