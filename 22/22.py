words = []
with open("p022_names.txt") as f:
  words = list(map(lambda s: s[1:], f.readlines()[0].split("\",")))

# there is an extra " hanging out there...
words[-1] = words[-1][:-1]

alphavalue = lambda c: ord(c)-ascii_offset+1
scores = []
ascii_offset = ord('A')
for i, name in enumerate(sorted(words)):
  alphavalues = map(alphavalue, name)
  alphavalues = list(alphavalues)
  score = (i+1) * sum(alphavalues)
  scores.append(score)

sum(scores)
