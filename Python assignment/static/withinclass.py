#Define a static variable and access that through an instance
class MyClass:
    static_variable = "Initial Value"  # Define a static variable

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    def change_static_instance(self, new_value):
        MyClass.static_variable = new_value  # Change static variable within instance
MyClass.static_variable = "Changed by Class"
print(" Static variable after change by class:", MyClass.static_variable)