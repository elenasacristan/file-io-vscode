import re
import collections

# https://www.w3schools.com/python/python_regex.asp

text = open('book.txt', encoding='utf-8').read().lower()
words = re.findall("\w+", text)
print(collections.Counter(words).most_common(20))
