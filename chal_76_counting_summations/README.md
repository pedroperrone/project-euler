# Counting Summations

The problem's page is [this](https://projecteuler.net/problem=76).

## Explaining the algorithm

Once the solution for the problem 31 (Coins Sum) was already done, solving this exercise was realy easy. We can reduce an instance of this problem to a Coins Sum instance where there is one coin value for each number between 1 and 99 and we want to sum 100. The range goes to 99 instead of 100 because using only the number 100 is not a valid sum according to the problem's description. Read the [Coins Sum solution](https://github.com/pedroperrone/project-euler/tree/master/chal_31_coins_sum) for more details.

## The answer

After running `python main.py 76` in the root of the project, we can see that the answer is `190569291`.
