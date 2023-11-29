class Parent1:
    def method1(self):
        return "Parent1's method called"

class Parent2:
    def method2(self):
        return "Parent2's method called"

class Child(Parent1, Parent2):
    pass

c = Child()
print(c.method1())
print(c.method2())