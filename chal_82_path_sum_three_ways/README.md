# Path Sum Two Ways Problem

The problem's page is [this](https://projecteuler.net/problem=82) and its definition is below:

## Explaining the algorithm

The solution for this problem is very similar to the [solution for the problem 81](https://github.com/pedroperrone/project-euler/tree/master/chal_81_path_sum_two_ways). The difference is that now you can make moviments throgh a column, so you have to run though it two times: one from top to bottom and another from bottom to top. The first iteration is the same as the solution for the problem 81, but the second only updates the sobsolutions matrix if the new solution is better than the old one.

## The answer

After running `python main.py 82` in the root of the project, we can see that the answer is `260324`.
