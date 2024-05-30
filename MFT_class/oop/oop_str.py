class Str:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        # print("here!", other)
        if isinstance(other, str):
            return Str(self.value + other)
        elif isinstance(other, int):
            return Str(self.value + str(other))
        else:
            return NotImplementedError
    def __str__(self) -> str:        
        return self.value

s = Str("hello")

s1 = 2

s4 = s + s1
print(s4)
