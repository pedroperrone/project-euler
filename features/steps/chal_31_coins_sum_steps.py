from behave import given, when, then, step
from chal_31_coins_sum.CoinsSum import CoinsSum

@given('I have entered {list_of_coins} into the problem instance')
def enter_list(context, list_of_coins):
    list_of_coins = [int(num) for num in list_of_coins.split(', ')]
    context.list_of_coins = list_of_coins

@given('I have also entered {target_value:d} into the problem instance')
def enter_target_value(context, target_value):
    context.target_value = target_value

@when('I press calculate_possibilities')
def calculate_possibilities(context):
    context.coins_sum_instance = CoinsSum(context.list_of_coins,
                                          context.target_value)
    context.result = context.coins_sum_instance.calculate_possibilities()

@then('the result should be {result:d}')
def check_result(context, result):
    assert context.result == result
