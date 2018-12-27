# Coin sums problem

The problem's page is [this](https://projecteuler.net/problem=31) and its definition is below:

```
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
```

## Explaining the algorithm

To solve this problem I used dynamic programming. Instead of using a bidimensional array I used a simple list overwriting its values to reduce the memory usage. The list has `target_value + 1` positions. `target_value` in Project Euler's instance of the problem is 200, because we want to know how many ways can 200p be made using any number of coins. The `+1` is for the 0 value. The position 0 is initialized and kept with `1`, because no matter what or how many coins you have, there is only one way to sum 0p (taking no coins).

The iterations were made throw the list of coins and, inside each iteration, there were other iterations throw the range from the `coin value` until the `target value`. In each calculation the logic was:

Without this coin we have `n` possibilities to sum `m` pences. If I take all the `p` possibilities to sum `(m - coin_value)` pences and combine each one of them with this new coin, I obtain `p` new ways to sum `m` pences. So, with this coin, there are `n + p` possibilities to sum `m` pences.

## The answer

After running `python main.py 31` in the root of the project, we can see that the answer is `73682`.
