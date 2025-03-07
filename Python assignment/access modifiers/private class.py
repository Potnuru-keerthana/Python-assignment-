class MyClass:
    def __init__(self):
        self.__private_field = 10  # Naming convention: double underscore
        
    def __private_method(self):
        print("This is a private method.")
        
    def public_method(self):
        print(self.__private_field)
        self.__private_method()

class SubClass(MyClass):
    def try_access(self):
        # Attempting to access private members (will cause AttributeError)
        # print(self.__private_field)
        # self.__private_method()
        pass

obj = MyClass()
obj.public_method()

sub_obj = SubClass()
sub_obj.try_access()