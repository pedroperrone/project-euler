# Path Sum Two Ways Problem

The problem's page is [this](https://projecteuler.net/problem=81) and its definition is below:

## Explaining the algorithm

To solve this problem I used dynamic programming. I used a matrix to save the subsolutions for the problem. The rule to fulfill the subsolution matrix were:
* If is the position 0-0, use the position 0-0 on the problem matrix;
* If the row is 0 and the column is `n`, use `subsolution[0][n - 1] + matrix[0][n]`
* If the row is `n` and the column is 0, use `subsolution[n - 1][0] + matrix[n][0]`
* Else, with row `n` and column `m`, use `min(subsolutions[n - 1][m], subsolutions[n][m - 1] + matrix[n][m])`

## The answer

After running `python main.py 81` in the root of the project, we can see that the answer is `427337`.
