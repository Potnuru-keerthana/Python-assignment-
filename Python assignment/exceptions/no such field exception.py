class MyClass:
    def __init__(self):
        self.name = "John"

try:
    obj = MyClass()
    print(obj.non_existent_attribute)  # This will raise an AttributeError
except AttributeError as e:
    print(f"NoSuchFieldException: {e}")
