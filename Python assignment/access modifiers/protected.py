class MyClass:
    def __init__(self):
        self._protected_field = 20  # Naming convention: single underscore
        
    def _protected_method(self):
        print("This is a protected method.")

class OtherClass:
    def access_protected(self, obj):
        print(obj._protected_field)
        obj._protected_method()

class SubClassDifferentPackage(MyClass):  # Simulate different package
    def access_protected(self):
        print(self._protected_field)
        self._protected_method()

obj = MyClass()
other_obj = OtherClass()
other_obj.access_protected(obj)

sub_obj_diff_pkg = SubClassDifferentPackage()
sub_obj_diff_pkg.access_protected()