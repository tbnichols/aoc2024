f =open('input.txt', 'r')
# f = open('sample2.txt', 'r')
from collections import defaultdict

import time
start_time = time.time()
conns = defaultdict(set)
visited = set()
for x in f:
    c1, c2 = x.strip().split('-')
    conns[c1].add(c2)
    conns[c2].add(c1)

def findclique(cset):
    maxlen = 0
    malpha = ""
    for c1 in cset:
        for c2 in conns[c1]:
            if c2 not in cset:
                fl = list(filter(lambda x: c2 not in conns[x], cset))
                # print(cset)
                # print(f"{c1}, {c2}, {fl}")
                if len(fl) ==0:
                    if frozenset(cset.union([c2])) not in visited:
                        leng, alpha = findclique(cset.union([c2]))
                        if leng >maxlen:
                            malpha = alpha
                            maxlen=leng
    visited.add(frozenset(cset))
    if maxlen ==0:
        return len(cset), sorted(list(cset))
    return maxlen, malpha

maxl = 0
ma  = ""
for comp1 in list(conns.keys()):
    l, a = findclique(set([comp1]))
    # print(l,a)
    if l>maxl:
        ma = a
        maxl=l


print(",".join(ma)) 
print("--- %s seconds ---" % (time.time() - start_time))