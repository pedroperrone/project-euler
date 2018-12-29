import unittest
from common.WordsListFormatter import WordsListFormatter
from chal_42_coded_triangle_numbers.CodedTriangleNumbers import CodedTriangleNumbers

class CodedTriangleNumbersTestCase(unittest.TestCase):
    def test_calculate_possibilities(self):
        words = WordsListFormatter.from_file('chal_42_coded_triangle_numbers/p042_words.txt')
        instance = CodedTriangleNumbers(words)
        self.assertEqual(instance.count_triangle_words(), 162)
