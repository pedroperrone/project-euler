Feature: CoinsSum

        Given a matrix with values

        I want to know the shortest path to go from left-top to right-bottom moving only right and down.

Scenario Outline: Calculate the shortest path

        Given I have entered <matrix_string> as the matrix

        When I press calculate_shortest_path

        Then the shortest_path should be <result>

 

        Examples:

            |                          matrix_string|   result|

            |                      1,2,3-4,5,6-7,8,9|       21|

            | 1,2,3,4-5,6,7,8-9,10,11,12-13,14,15,16|       46|
