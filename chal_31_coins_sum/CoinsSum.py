class CoinsSum:
    def __init__(self, coins_values, target_value):
        coins_values.sort()
        self.coins_values = coins_values
        self.target_value = target_value

    def calculate_possibilities(self):
        possibilities_for_ammount = [1] + [0] * (self.target_value)
        for coin in self.coins_values:
            for ammount in range(coin, self.target_value + 1):
                possibilities_for_ammount[ammount] += \
                    possibilities_for_ammount[ammount - coin]
        return possibilities_for_ammount[-1]
        
