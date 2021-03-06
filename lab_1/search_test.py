import unittest
from search import *


class TestSearch(unittest.TestCase):
    def test_linear_search(self):
        data = [1, 2, 3, 5, 6, 17, 12, 4]
        self.assertEqual(linear_search(data, 2), 1)
        self.assertEqual(linear_search(data, 9), -1)

    def test_binary_search(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(data, sorted(data))
        self.assertEqual(binary_search(data, 1, 0, len(data)-1), 0)
        self.assertEqual(binary_search(data, 14, 0, len(data)-1), -1)
        self.assertEqual(binary_search(data, -1, 0, len(data)-1), -1)
        self.assertEqual(binary_search(data, 2, 0, len(data)-1), 1)
        self.assertEqual(binary_search(data, 4, 0, len(data)-1), 3)


if __name__ == "__main__":
    unittest.main()
