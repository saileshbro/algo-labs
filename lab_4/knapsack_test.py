import unittest
from knapsack import greedyFractional, dynamicZeroOne, bruteforceZeroOne, bruteForceFractional


class KnapsackText(unittest.TestCase):
    def test_fractional(self):
        weights = [1, 2, 3]
        profits = [6, 10, 12]
        capacity = 5
        self.assertEqual(greedyFractional(weights, profits, capacity), 24)
        self.assertEqual(bruteForceFractional(
            weights, profits, capacity, len(weights)), 24)

    def test_zeroOne(self):
        weights = [10, 20, 30]
        profits = [60, 100, 120]
        capacity = 50
        self.assertEqual(dynamicZeroOne(weights, profits, capacity), 220)
        self.assertEqual(bruteforceZeroOne(
            weights, profits, capacity, len(weights)), 220)
        weights = []
        profits = []
        capacity = 50
        self.assertEqual(dynamicZeroOne(weights, profits, capacity), 0)
        self.assertEqual(bruteforceZeroOne(
            weights, profits, capacity, len(profits)), 0)
        profits = [50, 100, 150, 200]
        weights = [8, 16, 32, 40]
        capacity = 64
        self.assertEqual(dynamicZeroOne(weights, profits, capacity), 350)
        self.assertEqual(bruteforceZeroOne(
            weights, profits, capacity, len(weights)), 350)


if __name__ == "__main__":
    unittest.main()
