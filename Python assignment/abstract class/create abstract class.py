from abc import ABC, abstractmethod

# Abstract class with both abstract and non-abstract methods
class Animal(ABC):
    
    # Abstract method (no implementation)
    @abstractmethod
    def sound(self):
        pass
    
    # Non-abstract method with implementation
    def sleep(self):
        print("The animal is sleeping.")

# Child class inheriting from Animal class
class Dog(Animal):
    
    # Implementing the abstract method
    def sound(self):
        print("The dog barks.")

# Creating an object of Dog class (child class)
dog = Dog()

# Accessing the non-abstract method from the parent class (Animal)
dog.sleep()

# Creating an instance of Dog in Dog class and calling the abstract method
dog_instance = Dog()
dog_instance.sound()  # Calling the implemented abstract method

# Creating an instance of Dog in Dog class and calling the non-abstract method
dog_instance = Dog()
dog_instance.sleep()  # Calling the non-abstract method


