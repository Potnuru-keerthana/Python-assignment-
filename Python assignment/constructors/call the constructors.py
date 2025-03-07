class SuperClass:
    def __init__(self, message="SuperClass Constructor Called"):
        print(message)

class SubClass(SuperClass):
    def __init__(self, message="SubClass Constructor Called"):
        # Call the constructor of the superclass
        super().__init__("SuperClass Constructor Called via super()")
        print(message)

# Instantiate the child class
child = SubClass()
