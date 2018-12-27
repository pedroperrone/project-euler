import math

class Bhaskara:
    @staticmethod
    def get_roots(a, b, c):
        delta = pow(b, 2) - (4 * a * c)
        try:
            delta_root = math.sqrt(delta)
            first_root = Bhaskara.calculate_root(a, b, delta_root,
                                                 lambda x, y: x + y)
            second_root = Bhaskara.calculate_root(a, b, delta_root,
                                                  lambda x, y: x - y)
        except ValueError as e:
            first_root = math.nan
            second_root = math.nan
        finally:
            return (first_root, second_root)


    @staticmethod
    def calculate_root(a, b, delta_root, op):
        return op(-b, delta_root) / (2.0 * a)
