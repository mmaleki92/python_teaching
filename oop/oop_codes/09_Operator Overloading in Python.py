class Mango:
    def __init__(self,x):
        self.x = str(x)
    def __add__(self,y):
        return self.x + y.x
obj1 = Mango(7)
obj2 = Mango('mangoes')
print(obj1+obj2)