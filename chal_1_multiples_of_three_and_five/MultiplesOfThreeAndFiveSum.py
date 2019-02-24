import math

class MultiplesOfThreeAndFiveSum:
    def calculate_multiples_sum(self, limit):
        sums = [self.multiples_sum_for(n, limit - 1) for n in [3, 5, 15]]
        return sum(sums[0:-1]) - sums[-1]

    def multiples_sum_for(self, r, limit):
        number_of_elements = math.floor(limit / r) + 1
        return int(((number_of_elements - 1) * r) * number_of_elements / 2)
