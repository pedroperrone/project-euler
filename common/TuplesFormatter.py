class TuplesFormatter:
    @staticmethod
    def from_file(file_name):
        file = open(file_name, 'r')
        content = file.readlines()
        file.close()
        tuples = []
        for row in content:
            values = row.split(',')
            tuples.append((int(values[0]), int(values[1])))
        return tuples
