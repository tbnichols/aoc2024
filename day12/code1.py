f =open('input.txt', 'r')
# f = open('sample.txt', 'r')
from collections import defaultdict
grid = defaultdict(lambda: '.')
for i, x in enumerate(f):
    for j, y in enumerate(x.strip()):
        grid[(i,j)]=y
total=0
maxh=i
maxw=j
for x in range(maxh+1):
    for y in range(maxw+1):
        if grid[(x,y)] =='.':
            continue
        queue = [(x,y)]
        target = grid[(x,y)]
        perim = 0
        vandq = set([(x,y)])
        while len(queue) !=0:
            ele = queue.pop()
            a,b = ele
            for cand in [(a,b-1),(a,b+1),(a+1,b),(a-1,b)]:
                if grid[cand] == target:
                    if cand not in vandq:
                        vandq.add(cand)
                        queue.append(cand)
                else:
                    perim+=1
        total+= (perim * len(vandq))
        for ele in vandq:
            grid[ele]='.'

print(total)