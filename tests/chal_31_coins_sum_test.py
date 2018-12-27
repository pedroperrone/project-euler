import unittest
from chal_31_coins_sum.CoinsSum import CoinsSum

class CoinsSumTestCase(unittest.TestCase):
    def test_calculate_possibilities(self):
        instance = CoinsSum([1, 2, 5, 10, 20, 50, 100, 200], 200)
        self.assertEqual(instance.calculate_possibilities(), 73682)
