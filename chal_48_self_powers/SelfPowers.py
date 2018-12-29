class SelfPowers:
    def __init__(self, limit_value):
        self.limit_value = limit_value

    def sum_and_get_last_digits(self, amount_of_digits):
        powers_sum = sum([pow(n, n) for n in range(1, self.limit_value + 1)])
        return powers_sum % pow(10, amount_of_digits)
