f =open('input.txt', 'r')
# f = open('sample.txt', 'r')
from functools import reduce
ACACHE = {}
ECACHE = {}
total = 0
numgoals = {'7': (0,0), '8': (0,1), '9':(0,2),'4': (1,0), '5': (1,1), '6':(1,2),'1': (2,0), '2': (2,1), '3':(2,2), '0': (3,1), 'A': (3,2)}
dirgoals = {'^': (0,1), "A": (0,2), '<': (1,0), 'v':(1,1), '>':(1,2)}

def assemble(p, rem):
    if (p, rem) in ACACHE:
        return ACACHE[(p,rem)]
    length = 0
    for i, st in enumerate(p.split("A")[:-1]):
        length+= expand(st+"A", rem)
    ACACHE[(p,rem)] = length
    return length

def expand(ps, rem):
    if rem == 0:
        return len(ps)
    if (ps, rem) in ECACHE:
        return ECACHE[(ps, rem)]
    paths = set()
    paths.add(("", (0,2), ps))
    finalpaths = set()
    while len(paths)!=0:
        temppath = set()
        for acc, l, goals in paths: 
            if l == (0,0):
                continue
            if dirgoals[goals[0]] == l:
                if len(goals) ==1:
                    finalpaths.add(acc+"A")
                else:
                    temppath.add((acc+"A", l, goals[1:]))
            if dirgoals[goals[0]][1]>l[1]:
                temppath.add((acc+">", (l[0],l[1]+1), goals))
            if dirgoals[goals[0]][0]>l[0]:
                temppath.add((acc+"v", (l[0]+1,l[1]), goals))
            if dirgoals[goals[0]][1]<l[1]:
                temppath.add((acc+"<", (l[0],l[1]-1), goals))
            if dirgoals[goals[0]][0]<l[0]:
                temppath.add((acc+"^", (l[0]-1,l[1]), goals))
        paths=temppath
    minlen = -1
    for cand in finalpaths:
        if minlen == -1:
            minlen = assemble(cand, rem-1)
        else:
            minlen = min(minlen, assemble(cand,rem-1))
    ECACHE[(ps, rem)] = minlen
    return minlen
def numsolve(goal, loc):
    paths = set([("", loc)])
    while True:
        temppath = set()
        for p, l in paths:
            if l==(3,0):
                continue
            if goal[0]<l[0]:
                temppath.add((p+"^", (l[0]-1, l[1])))
            if goal[1]>l[1]:
                temppath.add((p+">", (l[0], l[1]+1)))
            if goal[0]>l[0]:
                temppath.add((p+"v", (l[0]+1, l[1])))
            if  goal[1]<l[1]:
                temppath.add((p+"<", (l[0], l[1]-1)))
        paths = temppath
        last = paths.pop()
        paths.add(last)
        if last[1] == goal:
            finalpath = set()
            for p in paths:
                finalpath.add((p[0]+"A", p[1]))
            paths=finalpath
            break
    return paths

iters = 25
for x in f:
    pointed = (3,2)
    presses = 0
    for y in x.strip():
        ord1 = {x[0] for x in numsolve(numgoals[y], pointed)}
        pointed = numgoals[y]
        mintot = -1
        for ordcand in ord1:
            if mintot == -1:
                mintot= assemble(ordcand,iters)
            else:
                mintot = min(mintot, assemble(ordcand, iters))
        presses += mintot
    total += presses * int(x.strip()[:-1])
print(total)
