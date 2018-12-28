import unittest
from chal_76_counting_summations.CountingSummations import CountingSummations

class CountingSummationsTestCase(unittest.TestCase):
    def test_calculate_possibilities(self):
        instance = CountingSummations(100)
        self.assertEqual(instance.calculate_possibilities(), 190569291)
