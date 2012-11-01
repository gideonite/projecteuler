#!/usr/bin/python

# 3 10 5 16 8 4 2 1


def collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3*n + 1

def make_seq(seq, dict):
    n = seq[0]

    if n == 1:
        for i in seq:
            dict[i] = seq.index(i) + 1
    elif dict.has_key(n):
        # a sequence that has already been seen
        _len = dict[n]
        for i in seq:
            dict[i] = seq.index(i) + _len
    else:
        make_seq([collatz(n)] + seq, dict)

    return dict

dict = {}
i = 2
#print make_seq([13], dict)[13]
#print make_seq([3], dict)[3]

while i < 1000000:
    dict = make_seq([i], dict)

    i += 1

maxKey, maxVal = 0, 0
for key in dict:
    if dict[key] > maxVal:
        maxKey, maxVal = key, dict[key]

print maxKey, maxVal
