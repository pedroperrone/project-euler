class WordsListFormatter:
    @staticmethod
    def from_file(file_name):
        file = open(file_name, 'r')
        content = '[' + file.read() + ']'
        file.close()
        return eval(content)
