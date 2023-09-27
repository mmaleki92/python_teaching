import unittest
from my_module import MyClass

class TestMyClass(unittest.TestCase):
    def test_init(self):
        my_class = MyClass()
        self.assertEqual(my_class.value, 0)

    def test_add(self):
        my_class = MyClass()
        my_class.add(1)
        self.assertEqual(my_class.value, 1)

if __name__ == '__main__':
    unittest.main()
