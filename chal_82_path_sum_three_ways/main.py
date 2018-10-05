from PathSumThreeWays import PathSumThreeWays
from MatrixFormatter import MatrixFormatter

matrix = MatrixFormatter.from_file('p082_matrix.txt')

sp = PathSumThreeWays(matrix)
print sp.calculate_shortest_path()
