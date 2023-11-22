class MyClass:
    @classmethod
    def class_method(cls):
        return "Class method called"

    @staticmethod
    def static_method():
        return "Static method called"

print(MyClass.class_method())
print(MyClass.static_method())