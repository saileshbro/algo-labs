import unittest
from search import *
from is_sorted import is_sorted


class TestSearch(unittest.TestCase):
    def test_linear_search(self):
        data = [1, 2, 3, 5, 6, 17, 12, 4]
        self.assertEqual(linear_search(data, 2), 1)
        self.assertEqual(linear_search(data, 9), -1)

    def test_binary_search(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(is_sorted(data), True)
        self.assertEqual(binary_search(data, 1,), 0)
        self.assertEqual(binary_search(data, 14), -1)
        self.assertEqual(binary_search(data, -1), -1)
        self.assertEqual(binary_search(data, 2), 1)
        self.assertEqual(binary_search(data, 4), 3)


if __name__ == "__main__":
    unittest.main()
