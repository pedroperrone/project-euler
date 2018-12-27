from chal_42_coded_triangle_numbers.TriangleNumber import TriangleNumber
import string

class CodedTriangleNumbers:
    def __init__(self, words):
        self.words = words

    def count_triangle_words(self):
        return len(list(filter(lambda w: self.is_triangle_word(w), self.words)))

    def is_triangle_word(self, word):
        return TriangleNumber.is_valid(self.word_as_number(word))

    def word_as_number(self, word):
        return sum([string.ascii_uppercase.index(char) + 1 for char in word])
