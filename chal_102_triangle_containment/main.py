from TrianglesContainment import TrianglesContainment
from TrianglesFormatter import TrianglesFormatter

triangles = TrianglesFormatter.from_file('p102_triangles.txt')
tc = TrianglesContainment(triangles)

print(tc.count_containing_origin())

