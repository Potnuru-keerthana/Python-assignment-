class Calculator:
    
    # Method with one parameter
    def add(self, a):
        return a + a
    
    # Method with two parameters
    def add(self, a, b):
        return a + b

# Creating an instance of the Calculator class
calc = Calculator()

# Calling methods with different numbers of parameters
print(calc.add(10, 5))  # Output: 15


class Printer:
    
    # Method with one integer parameter
    def print_value(self, value: int):
        print(f"Integer Value: {value}")
    
    # Method with one string parameter
    def print_value(self, value: str):
        print(f"String Value: {value}")

# Creating an instance of the Printer class
printer = Printer()

# Calling methods with different data types
printer.print_value(10)  # Output: Integer Value: 10
printer.print_value("Hello, world!")  # Output: String Value: Hello, world!


class Greeter:
    
    # Method to greet in English
    def greet(self, name: str):
        print(f"Hello, {name}!")
    
    # Method to greet in Spanish
    def greet(self, name: str):
        print(f"¡Hola, {name}!")

# Creating an instance of the Greeter class
greeter = Greeter()

# Calling the greet method
greeter.greet("Alice")  # Output: ¡Hola, Alice!
