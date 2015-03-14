words = []
with open("p022_names.txt") as f:
  words = list(map(lambda s: s[1:], f.readlines()[0].split("\",")))

words
