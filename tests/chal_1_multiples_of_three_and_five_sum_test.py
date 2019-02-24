import unittest
from chal_1_multiples_of_three_and_five.MultiplesOfThreeAndFiveSum import MultiplesOfThreeAndFiveSum

class MultiplesOfThreeAnfFiveSumTestCase(unittest.TestCase):
    def test_calculate_multiples_sim(self):
        instance = MultiplesOfThreeAndFiveSum()
        self.assertEqual(instance.calculate_multiples_sum(1000), 233168)
