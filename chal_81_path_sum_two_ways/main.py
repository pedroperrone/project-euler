from PathSumTwoWays import PathSumTwoWays
from MatrixFormatter import MatrixFormatter

matrix = MatrixFormatter.from_file('p081_matrix.txt')

sp = PathSumTwoWays(matrix)
print sp.calculate_shortest_path()
