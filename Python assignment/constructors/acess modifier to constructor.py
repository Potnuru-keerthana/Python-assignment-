class MyClass:
    def __init__(self):
        self.public_var = "Public Variable"
        self._protected_var = "Protected Variable"
        self.__private_var = "Private Variable"

    def display(self):
        print(f"Public: {self.public_var}")
        print(f"Protected: {self._protected_var}")
        print(f"Private: {self.__private_var}")

# Instantiate and access variables from outside the class
obj = MyClass()
obj.display()

# Access private and protected variables directly outside the class (not recommended)
print(f"Direct access to public: {obj.public_var}")
print(f"Direct access to protected: {obj._protected_var}")
# print(f"Direct access to private: {obj.__private_var}")  # Will raise an AttributeError
