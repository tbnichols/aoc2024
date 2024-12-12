f =open('input.txt', 'r')
# f = open('sample.txt', 'r')
from collections import defaultdict
grid = defaultdict(lambda: '.')
for i, x in enumerate(f):
    for j, y in enumerate(x.strip()):
        grid[(i,j)]=y
total=0
maxh=j
maxw=i
for x in range(maxh+1):
    for y in range(maxw+1):
        if grid[(x,y)] =='.':
            continue
        queue = [(x,y)]
        target = grid[(x,y)]
        vandq = set([(x,y)])
        while len(queue) !=0:
            ele = queue.pop()
            a,b = ele
            for cand in [(a,b-1),(a,b+1),(a+1,b),(a-1,b)]:
                if grid[cand] == target and cand not in vandq:
                    vandq.add(cand)
                    queue.append(cand)
        sides =0
        walls = defaultdict(set)
        n,e,s,w = list("nesw")
        for a,b in vandq:
            if (a+1,b) not in vandq:
                walls[s].add((a,b))
            if (a-1,b) not in vandq:
                walls[n].add((a,b))
            if (a,b+1) not in vandq:
                walls[e].add((a,b))
            if (a,b-1) not in vandq:
                walls[w].add((a,b))
        for dir, wl in walls.items():
            while len(wl)!=0:
                cur = wl.pop()
                ntemp = list(cur)
                stemp = list(cur)
                match dir:
                    case "e"|"w":
                        wl.add(cur)
                        while tuple(ntemp) in wl:
                            wl.discard(tuple(ntemp))
                            ntemp[0]-=1
                        wl.add(cur)
                        while tuple(stemp) in wl:
                            wl.discard(tuple(stemp))
                            stemp[0]+=1
                    case "s"|"n":
                        wl.add(cur)
                        while tuple(ntemp) in wl:
                            wl.discard(tuple(ntemp))
                            ntemp[1]-=1
                        wl.add(cur)
                        while tuple(stemp) in wl:
                            wl.discard(tuple(stemp))
                            stemp[1]+=1
                sides+=1

        print(f"{target}, {sides}, {len(vandq)}, {sides*len(vandq)}")
        total+= (sides * len(vandq))
        for ele in vandq:
            grid[ele]='.'

print(total)