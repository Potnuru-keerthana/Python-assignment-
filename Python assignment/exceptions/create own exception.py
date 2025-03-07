class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def check_value(value):
    if value < 0:
        raise MyCustomException("Negative value is not allowed")

try:
    check_value(-1)
except MyCustomException as e:
    print(f"Caught custom exception: {e}")
