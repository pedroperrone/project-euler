from WordsListFormatter import WordsListFormatter
from CodedTriangleNumbers import CodedTriangleNumbers

words = WordsListFormatter.from_file('p042_words.txt')
print(CodedTriangleNumbers(words).count_triangle_words())
