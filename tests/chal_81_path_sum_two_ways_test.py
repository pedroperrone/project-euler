import unittest
from chal_81_path_sum_two_ways.PathSumTwoWays import PathSumTwoWays
from common.MatrixFormatter import MatrixFormatter

class PathSumTwoWaysTestCase(unittest.TestCase):
    def test_calculate_possibilities(self):
        matrix = MatrixFormatter.from_file('chal_81_path_sum_two_ways/p081_matrix.txt')
        instance = PathSumTwoWays(matrix)
        self.assertEqual(instance.calculate_shortest_path(), 427337)
