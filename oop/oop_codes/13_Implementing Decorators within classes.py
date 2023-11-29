class MyClass:
    @staticmethod
    def method():
        return "Static method called"

    @classmethod
    def classmethod(cls):
        return "Class method called"

print(MyClass.method())
print(MyClass.classmethod())