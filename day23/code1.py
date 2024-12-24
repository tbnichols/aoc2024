f =open('input.txt', 'r')
# f = open('sample.txt', 'r')
from collections import defaultdict

conns = defaultdict(set)
tthrees = set()
for x in f:
    c1, c2 = x.strip().split('-')
    conns[c1].add(c2)
    conns[c2].add(c1)

for comp1 in conns:
    if comp1[0]!='t':
        continue
    for comp2 in conns[comp1]:
        for comp3 in conns[comp2]:
            if comp3 in conns[comp1]:
                tthrees.add(frozenset({comp1,comp2,comp3}))

print(len(tthrees)) 