class MyClass:
    def __init__(self, arg1=None, arg2=None):  # Default constructor with optional arguments
        if arg1 is None and arg2 is None:
            print("Default Constructor Called")
        elif arg2 is None:
            print(f"One Argument Constructor Called with argument: {arg1}")
        else:
            print(f"Two Argument Constructor Called with arguments: {arg1}, {arg2}")

# Main class to instantiate and call all constructors
class MainClass:
    def __init__(self):
        print("Instantiating MyClass with default constructor:")
        obj1 = MyClass()  # Default constructor
        
        print("\nInstantiating MyClass with one argument constructor:")
        obj2 = MyClass(10)  # One argument constructor
        
        print("\nInstantiating MyClass with two arguments constructor:")
        obj3 = MyClass(10, 20)  # Two arguments constructor

# Instantiate the main class to call all constructors
main = MainClass()
