f =open('input.txt', 'r')
# f = open('sample.txt', 'r')
from queue import PriorityQueue
from collections import defaultdict
from functools import reduce
grid = defaultdict(lambda: '#')
loc = ()
for i, x in enumerate(f):
    for j, y in enumerate(x.strip()):
        grid[(j,i)]=y
        if y == "S":
            loc = (j,i)

turns = {(1,0): [(0,1), (0,-1)], (0,1):[(1,0), (-1,0)], (-1,0):[(0,1), (0,-1)], (0,-1): [(1,0), (-1,0)]}
maxh=i
maxw=j
def mutate(location):
    return [(location[0]+x[0], location[1]+x[1]) for x in turns.keys() if 0<=location[0]+x[0]<=maxw and 0<location[1]+x[1]<=maxh]
finalcost = 0
pq = PriorityQueue()
visited = {}
pq.put((0, loc))
while pq.qsize()!=0:
    cost, l= pq.get()
    if l in visited:
        continue
    visited[l] = cost
    for mut in mutate(l):
        if grid[mut] != '#':
            pq.put((cost+1, mut))
skips = defaultdict(set)
print(visited)
for l, c in visited.items():
    mutlist=set([l])
    print(c)
    for i in range(20):
        tempmut = set()
        # print(i)
        # print(len(mutlist))
        for mut in reduce(list.__add__, map(mutate, mutlist)):
            tempmut.add(mut)
            if i>0:
                if grid[mut] != "#" and visited[mut]>c+i+1:
                    skips[visited[mut]-c-i-1].add((l,mut)) 
        mutlist = tempmut
# print(skips)
total =0
pathskips = set()
for i in sorted(skips.keys(), reverse=True):
    iskips = skips[i]
    iskips.difference_update(pathskips)
    print(f"{i}: {len(iskips)}")
    pathskips.update(skips[i])
    if i>=100:
        total+=len(iskips)
    
print(total)