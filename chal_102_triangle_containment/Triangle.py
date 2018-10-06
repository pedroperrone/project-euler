from math import atan2
from Point import Point
from Vector import Vector

class Triangle():
    def __init__(self, point_a, point_b, point_c):
        center = Point((point_a.x + point_b.x + point_c.x) / 3, \
                       (point_a.y + point_b.y + point_c.y) / 3)
        self.points = [point_a, point_b, point_c]
        self.points.sort(key = lambda p: atan2(p.x - center.x, p.y - center.y))

    def include(self, point):
        return all(self.not_on_line_left(line, point) for line in range(0, 3))

    def not_on_line_left(self, line_index, point):
        if line_index is len(self.points) - 1:
            point_a = self.points[0]
            point_b = self.points[-1]
        else:
            point_a = self.points[line_index + 1]
            point_b = self.points[line_index]
        line_vector = Vector.by_points_subtraction(point_a, point_b)
        orthogonal_vector = line_vector.orthogonal_vector()
        point_vector = Vector.by_points_subtraction(point, point_b)
        return Vector.dot_product(point_vector, orthogonal_vector) >= 0
