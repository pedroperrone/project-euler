import unittest
from chal_48_self_powers.SelfPowers import SelfPowers

class SelfPowersTestCase(unittest.TestCase):
    def test_sum_and_get_last_digits(self):
        instance = SelfPowers(1000)
        self.assertEqual(instance.sum_and_get_last_digits(10), 9110846700)
