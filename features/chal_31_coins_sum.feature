Feature: CoinsSum

        Given a list of coins and a target value

        I want to know how many possibilities do sum that values with the coins exist.

Scenario Outline: Calculare the ammount of possibilities to sum a value with coins

        Given I have entered <list_of_coins> into the problem instance

        And I have also entered <target_value> into the problem instance

        When I press calculate_possibilities

        Then the result should be <result>

 

        Examples:

            |  list_of_coins|  target_value|   result|

            |              1|            10|        1|

            |    1, 2, 5, 10|            10|       11|

            |    1, 5, 2, 10|            10|       11|
