from collections.abc import Iterable

def get_length(item):
    if isinstance(item, Iterable):
        return len(item)
    else:
        return "Not iterable"

print(get_length("Hello"))
print(get_length([1, 2, 3]))
print(get_length(123))