class A:
    def method_a1(self):
        print("Method A1")

    def method_a2(self):
        print("Method A2")

    def override_method(self):
        print("Override method in A")

class B(A):
    def method_b1(self):
        print("Method B1")

    def method_b2(self):
        print("Method B2")

    def override_method(self):
        print("Override method in B")

class C(B):
    def method_c1(self):
        print("Method C1")

    def method_c2(self):
        print("Method C2")

    def override_method(self):
        print("Override method in C")

# Create objects and call methods
a = A()
b = B()
c = C()

a.method_a1()
a.method_a2()
a.override_method()

b.method_a1()  # Inherited from A
b.method_a2()  # Inherited from A
b.method_b1()
b.method_b2()
b.override_method()

c.method_a1()  # Inherited from A
c.method_a2()  # Inherited from A
c.method_b1()  # Inherited from B
c.method_b2()  # Inherited from B
c.method_c1()
c.method_c2()
c.override_method()

# Call overridden method with superclass reference
a_ref_b = B()
a_ref_c = C()

a_ref_b.override_method()
a_ref_c.override_method()

# Runtime Polymorphism with Data Members
class A_data:
    data = "A data"

    def show_data(self):
        print(self.data)

class B_data(A_data):
    data = "B data"

class C_data(B_data):
    data = "C data"

a_data = A_data()
b_data = B_data()
c_data = C_data()

a_data.show_data()
b_data.show_data()
c_data.show_data()

a_ref_b_data = B_data()
a_ref_c_data = C_data()

a_ref_b_data.show_data()
a_ref_c_data.show_data()