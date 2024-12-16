f =open('input.txt', 'r')
# f = open('sample2.txt', 'r')
from queue import PriorityQueue
from collections import defaultdict
grid = defaultdict(lambda: '.')
loc = ()
for i, x in enumerate(f):
    for j, y in enumerate(x.strip()):
        grid[(j,i)]=y
        if y == "S":
            loc = (j,i)
maxh=i
maxw=j
finalcost = 9999999999
turns = {(1,0): [(0,1), (0,-1)], (0,1):[(1,0), (-1,0)], (-1,0):[(0,1), (0,-1)], (0,-1): [(1,0), (-1,0)]}
pq = PriorityQueue()
visited = {}
inpath = set()
pq.put((0, loc, (1,0), [loc]))
total = 0
while pq.not_empty:
    cost, l, dir, path = pq.get()
    if cost > finalcost:
        break
    if (l, dir) in visited and visited[(l,dir)]<cost:
        continue
    visited[(l, dir)] = min(cost, visited.get((l,dir), 9999999))
    if grid[l] == 'E':
        finalcost = cost
        print(path)
        inpath.update(path)
        inpath.add(l)
    if grid[(l[0]+dir[0], l[1]+dir[1])] != '#':
        if cost+1>82460:
            continue
        pq.put((cost+1, (l[0]+dir[0], l[1]+dir[1], ), dir, path[:]+[l]))
    for newdir in turns[dir]:
        if cost +1000 > 82460:
            break
        pq.put((cost+1000, l, newdir, path[:])) 
    if total %10000 ==0:
        print(cost)
    total +=1
print(finalcost)
print(len(inpath))
