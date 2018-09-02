class PathSumTwoWays():
    def __init__(self, matrix):
        lists_length = len(matrix[0])
        if not all(len(row) == lists_length for row in matrix):
            raise ValueError('Invalid matrix')
        self.paths_matrix = matrix
        self.lists_length = lists_length

    def calculate_shortest_path(self):
        self.__initialize_subsolutions_matrix()
        for row_index in self.__paths_matrix_range():
            for column_index in self.__columns_range():
                self.subsolutions[row_index][column_index] = \
                    self.__best_solution_for(row_index, column_index)
        return self.subsolutions[-1][-1]

    def __initialize_subsolutions_matrix(self):
        self.subsolutions = []
        for row in self.__paths_matrix_range():
            self.subsolutions.append([0] * len(self.paths_matrix))

    def __paths_matrix_range(self):
        return range(0, len(self.paths_matrix))

    def __columns_range(self):
        return range(0, self.lists_length)

    def __best_solution_for(self, row_index, column_index):
        if row_index is 0 and column_index is 0:
            return self.paths_matrix[0][0]
        left_value = self.__cost_value_at_left_position(row_index, column_index)
        top_value = self.__cost_value_at_top_position(row_index, column_index)
        current_position_value = self.paths_matrix[row_index][column_index]
        return min(left_value, top_value) + current_position_value

    def __cost_value_at_left_position(self, row, column):
        if column is 0:
            return float("inf")
        return self.subsolutions[row][column - 1]

    def __cost_value_at_top_position(self, row, column):
        if row is 0:
            return float("inf")
        return self.subsolutions[row - 1][column]


