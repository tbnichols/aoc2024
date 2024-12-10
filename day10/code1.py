f =open('input.txt', 'r')
#f = open('sample.txt', 'r')
from collections import defaultdict
grid = defaultdict(lambda: -1)
i=0
j=0
total = 0
for i, x in enumerate(f):
    for j, y in enumerate(x.strip()):
        grid[(i,j)]=int(y)
maxh=i
maxw=j
for x in range(maxh+1):
    for y in range(maxw+1):
        if grid[(x,y)] !=0:
            continue
        queue = set([(x,y)])
        target =0
        while len(queue) !=0 and target !=10:
            #print(f"{x},{y},{target},{queue}")
            tempqueue = set() 
            for ele in queue:
                if grid[ele] == target:
                    if target ==9:
                        total +=1
                    else:
                        a,b = ele
                        tempqueue.update([(a,b-1),(a,b+1),(a+1,b),(a-1,b)])
            queue = tempqueue
            target+=1
        print(f"{x},{y}, {total}")

print(total)
