from Triangle import Triangle
from Point import Point

class TrianglesFormatter:
    @staticmethod
    def from_file(file_name):
        file = open(file_name, 'r')
        file_content = file.readlines()
        matrix = []
        for row in file_content:
            coordinates = [int(c) for c in row.split(",")]
            point_a = Point(coordinates[0], coordinates[1])
            point_b = Point(coordinates[2], coordinates[3])
            point_c = Point(coordinates[4], coordinates[5])
            matrix.append(Triangle(point_a, point_b, point_c))
        return matrix
