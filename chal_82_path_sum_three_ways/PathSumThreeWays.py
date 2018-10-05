class PathSumThreeWays():
    def __init__(self, matrix):
        lists_length = len(matrix[0])
        if not all(len(row) == lists_length for row in matrix):
            raise ValueError('Invalid matrix')
        self.paths_matrix = matrix
        self.lists_length = lists_length

    def calculate_shortest_path(self):
        self.__initialize_subsolutions_matrix()
        for column in self.__columns_range():
            for row in self.__paths_matrix_range():
                self.subsolutions[row][column] = \
                    self.__best_solution_from_top(row, column)

            for row in self.__reversed_path_matrix_range():
                self.subsolutions[row][column] =  \
                    self.__best_solution_from_bottom(row, column)
        return min([self.subsolutions[v][-1] for v in  \
                                              range(0, len(self.paths_matrix))])

    def __initialize_subsolutions_matrix(self):
        self.subsolutions = []
        for row in self.__paths_matrix_range():
            self.subsolutions.append([float("inf")] * len(self.paths_matrix))

    def __paths_matrix_range(self):
        return range(0, len(self.paths_matrix))

    def __reversed_path_matrix_range(self):
        return list(reversed(self.__paths_matrix_range()))

    def __columns_range(self):
        return range(0, self.lists_length)

    def __best_solution_from_top(self, row_index, column_index):
        if column_index is 0:
            return self.paths_matrix[row_index][0]
        above_cost = self.__cost_value_above(row_index, column_index)
        left_cost = self.__cost_value_at_left_position(row_index, column_index)
        current_position_cost = self.paths_matrix[row_index][column_index]
        return min(above_cost, left_cost) + current_position_cost

    def __best_solution_from_bottom(self, row_index, column_index):
        if column_index is 0:
            return self.paths_matrix[row_index][column_index]
        below_cost = self.__cost_value_below(row_index, column_index)
        left_cost = self.__cost_value_at_left_position(row_index, column_index)
        current_position_cost = self.paths_matrix[row_index][column_index]
        potential_solution = min(below_cost, left_cost) + current_position_cost
        current_solution = self.subsolutions[row_index][column_index]
        return min(potential_solution, current_solution)

    def __cost_value_at_left_position(self, row, column):
        if column is 0:
            return float("inf")
        return self.subsolutions[row][column - 1]

    def __cost_value_above(self, row, column):
        if row is 0:
            return float("inf")
        return self.subsolutions[row - 1][column]

    def __cost_value_below(self, row, column):
        if row is (self.lists_length - 1):
            return float("inf")
        return self.subsolutions[row + 1][column]
