# This unit test tests the sum() function to ensure that it works correctly with two numbers and an empty list.
import unittest

class TestSum(unittest.TestCase):
    def test_sum_of_two_numbers(self):
        self.assertEqual(sum([1, 2]), 3)

    def test_sum_of_empty_list(self):
        self.assertEqual(sum([]), 0)

if __name__ == '__main__':
    unittest.main()
