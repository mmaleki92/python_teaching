def apply_func(func, arg):
    return func(arg)

def square(x):
    return x**2

result = apply_func(square, 5)
print(result)