# Coded Triangle Numbers Problem

The problem's page is [this](https://projecteuler.net/problem=42).

## Explaining the algorithm

The solution for this problem is easy after some algebric manipulation. We can turn the expression `tn = 1/2 * n * (n + 1)` into `0 = 1/2 * n^2 + 1/2 * n - tn` and treat `tn` as a constant. For each word in the file, we calculate its value and replace the constant `tn` by the given value. Then, we calculate the value of `n` with the simple Bhaskara expression. Once we are interested only in natural values, we can discart the negative root. If the positive one is an integer number, then the word value is a triangle number.

## The answer

After running `python main.py 42` in the root of the project, we can see that the answer is `162`.
