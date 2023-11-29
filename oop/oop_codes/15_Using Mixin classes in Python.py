class Mixin1(object):
    def test(self):
        print("Mixin1")

class Mixin2(object):
    def test(self):
        print("Mixin2")

class MyClass(Mixin1, Mixin2):
    pass

obj = MyClass()
obj.test()