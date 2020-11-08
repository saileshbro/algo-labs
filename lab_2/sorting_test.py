import unittest
from sorting import insertion_sort, merge_sort


class TestSorting(unittest.TestCase):
    def test_insertion_sort(self):
        data = [14, 2, 8, 6, 1, 3, 5]
        sorted = [1, 2, 3, 5, 6, 8, 14]
        insertion_sort(data)
        self.assertListEqual(data, sorted)
        data = []
        sorted = []
        insertion_sort(data)
        self.assertListEqual(data, sorted)

    def test_merge_sort(self):
        data = [14, 2, 8, 6, 1, 3, 5]
        sorted = [1, 2, 3, 5, 6, 8, 14]
        merge_sort(data, 0, len(data))
        data = [14, 2, 8, 6, 1, 3, 5]
        sorted = [2, 8, 14, 6, 1, 3, 5]
        merge_sort(data, 0, 3)
        self.assertListEqual(data, sorted)


if __name__ == "__main__":
    unittest.main()
