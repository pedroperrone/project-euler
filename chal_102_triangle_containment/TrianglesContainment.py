from Point import Point

class TrianglesContainment():
    def __init__(self, triangles):
        self.triangles = triangles

    def count_containing_origin(self):
        counter = 0
        origin = Point(0, 0)
        for triangle in self.triangles:
            if triangle.include(origin):
                counter += 1
        return counter
