import math

class LargestExponential:
    def __init__(self, base_and_exponent_tuples):
        self.base_and_exponent_tuples = base_and_exponent_tuples

    def find_greatest_value_index(self, index_base = 1):
        max_value = max(self.base_and_exponent_tuples, key = self.find_max_function())
        return self.base_and_exponent_tuples.index(max_value) + index_base

    def find_max_function(self):
        return lambda tuple: tuple[1] * math.log(tuple[0])
