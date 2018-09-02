from behave import given, when, then, step
from chal_81_path_sum_two_ways.PathSumTwoWays import PathSumTwoWays

@given('I have entered {matrix_string} as the matrix')
def enter_list(context, matrix_string):
    matrix = [[int(num) for num in row.split(',')] for row in matrix_string.split('-')]
    context.matrix = matrix

@when('I press calculate_shortest_path')
def calculate_possibilities(context):
    context.path_sum_two_ways_instance = PathSumTwoWays(context.matrix)
    context.result = context.path_sum_two_ways_instance.calculate_shortest_path()

@then('the shortest_path should be {result:d}')
def check_result(context, result):
    assert context.result == result
