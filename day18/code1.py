f =open('input.txt', 'r')
# f = open('sample.txt', 'r')
from queue import PriorityQueue
from collections import defaultdict
grid = defaultdict(lambda: '.')
loc = ()
cards = [(1,0),(0,1),(0,-1),(-1,0)]
for i, x in enumerate(f):
    if i ==1024:
        break
    grid[(tuple(list(map(int, x.strip().split(",")))))]='X'
loc = (0,0)
maxh=70
maxw=70

for i in range(maxh+1):
    grid[(-1,i)]='X'
    grid[(maxh+1, i)]='X'
    grid[(i,-1)]='X'
    grid[(i, maxh+1)]='X'

grid[(maxw,maxh)] = "E"
print(grid)
finalcost = 0
pq = PriorityQueue()
visited = set()

# def minsteps(l, path,cost):
    # if grid[l] == 'E':

pq.put((0, loc))
while pq.qsize()!=0:
    cost, l = pq.get(False)
    if l in visited:
        continue
    visited.add(l)
    if grid[l] == 'E':
        finalcost = cost
        break
    for card in cards:
        if grid[(l[0]+card[0], l[1]+card[1])] != 'X':
            pq.put((cost+1, (l[0]+card[0], l[1]+card[1])))
print(finalcost)
