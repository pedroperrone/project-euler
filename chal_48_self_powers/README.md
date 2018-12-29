# Coded Triangle Numbers Problem

The problem's page is [this](https://projecteuler.net/problem=48).

## Explaining the algorithm

Python is a great tool to solve this problem. Using languages like C would bring us problems because the numbers in the challenge are way greater than `unsigned long long int` (64 bits, wich represents numbers until 2^64 - 1). Python, instead, can treat integers as software, so the representation limit is the memory available. Therefore, resolving the summatory and taking the last 10 digits works fine.

## The answer

After running `python main.py 48` in the root of the project, we can see that the answer is `9110846700`.
