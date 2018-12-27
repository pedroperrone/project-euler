import sys
from chal_31_coins_sum.CoinsSum import CoinsSum
from chal_42_coded_triangle_numbers.CodedTriangleNumbers import CodedTriangleNumbers
from chal_81_path_sum_two_ways.PathSumTwoWays import PathSumTwoWays
from chal_82_path_sum_three_ways.PathSumThreeWays import PathSumThreeWays
from chal_102_triangle_containment.TrianglesContainment import TrianglesContainment

from common.MatrixFormatter import MatrixFormatter
from common.TrianglesFormatter import TrianglesFormatter
from common.WordsListFormatter import WordsListFormatter

def run_challenge_31():
    cs = CoinsSum([1, 2, 5, 10, 20, 50, 100, 200], 200)
    print(cs.calculate_possibilities())

def run_challenge_42():
    words = WordsListFormatter.from_file('chal_42_coded_triangle_numbers/p042_words.txt')
    print(CodedTriangleNumbers(words).count_triangle_words())

def run_challenge_81():
    matrix = MatrixFormatter.from_file('chal_81_path_sum_two_ways/p081_matrix.txt')
    ps = PathSumTwoWays(matrix)
    print(ps.calculate_shortest_path())

def run_challenge_82():
    matrix = MatrixFormatter.from_file('chal_82_path_sum_three_ways/p082_matrix.txt')
    ps = PathSumThreeWays(matrix)
    print(ps.calculate_shortest_path())

def run_challenge_102():
    triangles = TrianglesFormatter.from_file('chal_102_triangle_containment/p102_triangles.txt')
    tc = TrianglesContainment(triangles)
    print(tc.count_containing_origin())

challenges = {
    31: run_challenge_31,
    42: run_challenge_42,
    81: run_challenge_81,
    82: run_challenge_82,
    102: run_challenge_102
}

try:
    challenges[int(sys.argv[1])]()
except KeyError as e:
    print('The challenge with the given number was not completed.')
except ValueError as e:
    print('Please, insert a valid number as parameter')
