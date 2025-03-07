# Define a static variable and change within the class
class MyClass:
    static_variable = "Initial Value"  # Define a static variable

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    def change_static_instance(self, new_value):
        MyClass.static_variable = new_value  # Change static variable within instance
instance1 = MyClass("Instance Variable 1")
instance1.change_static_instance("Changed by Instance 1")
print(" Static variable after change by instance:", MyClass.static_variable)