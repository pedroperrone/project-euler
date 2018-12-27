class MatrixFormatter:
    @staticmethod
    def from_file(file_name):
        file = open(file_name, 'r')
        file_content = file.readlines()
        file.close()
        matrix = []
        for row in file_content:
            matrix.append([])
            for column in row.split(','):
                matrix[-1].append(int(column))
        return matrix
