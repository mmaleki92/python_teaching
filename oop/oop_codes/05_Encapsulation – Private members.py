class MyClass:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"

obj = MyClass()
print(obj.public)
print(obj._protected)
print(obj.__private)  # This will raise an AttributeError