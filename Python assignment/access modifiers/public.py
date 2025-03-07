class MyClass:
    def __init__(self):
        self.public_field = 30  # No underscore prefix
        
    def public_method(self):
        print("This is a public method.")

class OtherClass:
    def access_public(self, obj):
        print(obj.public_field)
        obj.public_method()

class SubClassDifferentPackage(MyClass):  # Simulate different package
    def access_public(self):
        print(self.public_field)
        self.public_method()

obj = MyClass()
other_obj = OtherClass()
other_obj.access_public(obj)

sub_obj_diff_pkg = SubClassDifferentPackage()
sub_obj_diff_pkg.access_public()