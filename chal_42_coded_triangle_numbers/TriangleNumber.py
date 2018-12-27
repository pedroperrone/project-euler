import math
from Bhaskara import Bhaskara

class TriangleNumber:
    @staticmethod
    def is_valid(triangle_number):
        root = max(Bhaskara.get_roots(0.5, 0.5, -triangle_number))
        return root.is_integer()
