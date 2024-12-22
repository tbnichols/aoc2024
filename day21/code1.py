# f =open('input.txt', 'r')
f = open('sample.txt', 'r')
from functools import reduce

total = 0
numgoals = {'7': (0,0), '8': (0,1), '9':(0,2),'4': (1,0), '5': (1,1), '6':(1,2),'1': (2,0), '2': (2,1), '3':(2,2), '0': (3,1), 'A': (3,2)}
dirgoals = {'^': (0,1), "A": (0,2), '<': (1,0), 'v':(1,1), '>':(1,2)}
def expand(ps):
    paths = set()
    for i in ps:
        paths.add(("", (0,2), i))
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
    return finalpaths
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


for x in f:
    pointed = (3,2)
    presses = 0
    for y in x.strip():
        ord1 = {x[0] for x in numsolve(numgoals[y], pointed)}
        pointed = numgoals[y]
        print(ord1)
        ord2 = expand(ord1)
        print(ord2)
        ord3 = expand(ord2)
        print(ord3)
        presses += reduce(min, map(lambda x: len(x), ord3))
        print(presses)
        input()
    total += presses * int(x.strip()[:-1])
print(total)
        




