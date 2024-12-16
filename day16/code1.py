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
finalcost = 0
turns = {(1,0): [(0,1), (0,-1)], (0,1):[(1,0), (-1,0)], (-1,0):[(0,1), (0,-1)], (0,-1): [(1,0), (-1,0)]}
pq = PriorityQueue()
visited = set()
pq.put((0, loc, (1,0)))
while pq.not_empty:
    cost, l, dir = pq.get()
    if (l, dir) in visited:
        continue
    visited.add((l, dir))
    if grid[l] == 'E':
        finalcost = cost
        break
    if grid[(l[0]+dir[0], l[1]+dir[1])] != '#':
        pq.put((cost+1, (l[0]+dir[0], l[1]+dir[1]), dir))
    for newdir in turns[dir]:
        pq.put((cost+1000, l, newdir)) 
print(finalcost)
