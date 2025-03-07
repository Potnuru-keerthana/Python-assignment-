class Person:
    def __init__(self, name, age):
        # Constructor attributes
        self.name = name
        self.age = age
        print(f"Person Constructor Called! Name: {self.name}, Age: {self.age}")

# Instantiating the class to demonstrate constructor attributes
person1 = Person("John", 30)
person2 = Person("Alice", 25)
