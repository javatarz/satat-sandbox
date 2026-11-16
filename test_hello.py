import unittest

from hello import greet, hello


class HelloTest(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello, world!")


class GreetTest(unittest.TestCase):
    def test_greet_returns_greeting(self):
        self.assertEqual(greet("Karun"), "Hello, Karun!")

    def test_greet_empty_name_raises(self):
        with self.assertRaises(ValueError):
            greet("")


if __name__ == "__main__":
    unittest.main()
