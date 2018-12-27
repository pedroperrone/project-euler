class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def orthogonal_vector(self):
        x = self.y
        y = -self.x
        return Vector(x, y)

    @staticmethod
    def by_points_subtraction(point_a, point_b):
        x = point_a.x - point_b.x
        y = point_a.y - point_b.y
        return Vector(x, y)

    @staticmethod
    def dot_product(vector_a, vector_b):
        return (vector_a.x * vector_b.x) + (vector_a.y * vector_b.y)
