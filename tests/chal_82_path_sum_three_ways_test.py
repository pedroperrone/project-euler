import unittest
from chal_82_path_sum_three_ways.PathSumThreeWays import PathSumThreeWays
from common.MatrixFormatter import MatrixFormatter

class PathSumThreeWaysTestCase(unittest.TestCase):
    def test_calculate_possibilities(self):
        matrix = MatrixFormatter.from_file('chal_82_path_sum_three_ways/p082_matrix.txt')
        instance = PathSumThreeWays(matrix)
        self.assertEqual(instance.calculate_shortest_path(), 260324)
