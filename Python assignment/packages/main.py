# file: mypackage/class1.py
class Class1:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello from {self.name}!"
# file: mypackage/class2.py
class Class2:
    def __init__(self, name):
        self.name = name

    def farewell(self):
        return f"Goodbye from {self.name}!"
# file: mypackage/__init__.py
        from .class1 import Class1
        from .class2 import Class2
# file: main.py
        from mypackage import Class1, Class2

# Create objects of both classes
obj1 = Class1("Class1")
obj2 = Class2("Class2")

# Call their methods
print(obj1.greet())  # Output: Hello from Class1!
print(obj2.farewell())  # Output: Goodbye from Class2!

