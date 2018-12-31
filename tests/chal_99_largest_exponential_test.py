import unittest
from chal_99_largest_exponential.LargestExponential import LargestExponential
from common.TuplesFormatter import TuplesFormatter

class LargestExponentialTestCase(unittest.TestCase):
    def test_find_greatest_value_index(self):
        values = TuplesFormatter.from_file('chal_99_largest_exponential/p099_base_exp.txt')
        instance = LargestExponential(values)
        self.assertEqual(instance.find_greatest_value_index(), 709)
