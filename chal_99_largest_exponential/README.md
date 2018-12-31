# Largest Exponential

The problem's page is [this](https://projecteuler.net/problem=99) and its definition is below:

## Explaining the algorithm

Although Python can calculate the values present on the problem, it would take too much time. However, we dont't need to actually calculate the values to know which one is the biggest. When comparing two numbers, we can calculate the logarithm in the same base for both and compare the new values. Yet, it is possible to use the property bellow to process the exponent.

![Logarithm property](https://i.ibb.co/BGt1Ljp/Captura-de-Tela-2018-12-31-s-19-20-40.png)

With this we can calculate the log of the base and multiply it by the exponent. Comparing the result of this equation applied to each row, we can figure out which one is the greatest.

## The answer

After running `python main.py 99` in the root of the project, we can see that the answer is `709`.
