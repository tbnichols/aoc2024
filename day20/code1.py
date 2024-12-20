f =open('input.txt', 'r')
# f = open('sample.txt', 'r')
from queue import PriorityQueue
from collections import defaultdict
grid = defaultdict(lambda: '#')
loc = ()
for i, x in enumerate(f):
    for j, y in enumerate(x.strip()):
        grid[(j,i)]=y
        if y == "S":
            loc = (j,i)

turns = {(1,0): [(0,1), (0,-1)], (0,1):[(1,0), (-1,0)], (-1,0):[(0,1), (0,-1)], (0,-1): [(1,0), (-1,0)]}
def mutate(location):
    return [(location[0]+x[0], location[1]+x[1]) for x in turns.keys()]
maxh=i
maxw=j
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
skips = defaultdict(list)
print(visited)
for l, c in visited.items():
    for mut in mutate(l):
        if l == (7,1):
            print(mut)
        if grid[mut] =='#':
            for mut2 in mutate(mut):
                if l == (7,1):
                    print(f"{l}, {mut}, {mut2}, {visited.get(mut2, '#')}, {c}")
                if mut2!=l and grid[mut2] != "#" and visited[mut2]>c+2:
                    skips[visited[mut2]-c-2].append((l,mut2)) 
print(skips)
total =0
for i, j in skips.items():
    print(f"{i}: {len(j)}")
    if i>=100:
        total+=len(j)
print(total)