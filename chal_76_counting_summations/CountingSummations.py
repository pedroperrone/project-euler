from chal_31_coins_sum.CoinsSum import CoinsSum

class CountingSummations(CoinsSum):
    def __init__(self, target_value):
        range_as_list = [n for n in range(1, target_value)]
        super().__init__(range_as_list, target_value)
