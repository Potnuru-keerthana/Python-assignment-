try:
    # Attempt division by zero
    x = 10
    y = 0
    result = x / y
    print(result)
except ZeroDivisionError as e:
    print(f"Arithmetic Exception: {e}")
