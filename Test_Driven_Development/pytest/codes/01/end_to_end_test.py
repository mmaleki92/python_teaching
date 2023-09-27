import unittest
from my_app import MyApp

class TestMyApp(unittest.TestCase):
    def test_login(self):
        my_app = MyApp()
        my_app.login('username', 'password')
        self.assertTrue(my_app.is_logged_in())

if __name__ == '__main__':
    unittest.main()
