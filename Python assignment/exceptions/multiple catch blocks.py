try:
    # Try to perform different operations that could raise multiple exceptions
    x = 10
    y = "string"
    result = x + y  # This will raise TypeError
except ZeroDivisionError as e:
    print(f"Caught ZeroDivisionError: {e}")
except TypeError as e:
    print(f"Caught TypeError: {e}")
except Exception as e:
    print(f"Caught General Exception: {e}")
