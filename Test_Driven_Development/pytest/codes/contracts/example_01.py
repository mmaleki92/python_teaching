from contracts import natural, positive_integer, compose
from contracts import ic, natural

@ic(val = compose(natural, positive_integer))
def func(val):
    return val


func(-1)

