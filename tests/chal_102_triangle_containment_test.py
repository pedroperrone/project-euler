import unittest
from chal_102_triangle_containment.TrianglesContainment import TrianglesContainment
from common.TrianglesFormatter import TrianglesFormatter

class TrianglesContainmentTestCase(unittest.TestCase):
    def test_count_containing_origin(self):
        matrix = TrianglesFormatter.from_file('chal_102_triangle_containment/p102_triangles.txt')
        instance = TrianglesContainment(matrix)
        self.assertEqual(instance.count_containing_origin(), 228)
