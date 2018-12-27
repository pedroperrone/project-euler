import math
from chal_42_coded_triangle_numbers.Bhaskara import Bhaskara

class TriangleNumber:
    @staticmethod
    def is_valid(triangle_number):
        root = max(Bhaskara.get_roots(0.5, 0.5, -triangle_number))
        return root.is_integer()
