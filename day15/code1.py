f =open('input.txt', 'r')
# f = open('sample2.txt', 'r')
from collections import defaultdict

mapping = True
grid = defaultdict(lambda : ".")
cury=0
loc = ()
dirs = {"<": (-1,0), "^": (0,-1), ">":(1,0), "v": (0,1)}
for x in f:
    if mapping and x.strip() =='':
        mapping = False
        continue
    elif mapping:
        for curx, val in enumerate(x.strip()):
            grid[(curx,cury)] = val
            if val == '@':
                loc = (curx, cury)
        cury+=1
    else:
        for ins in x.strip():
            temploc = loc
            while grid[temploc] not in [".", "#"]:
                temploc = (temploc[0]+dirs[ins][0], temploc[1]+dirs[ins][1])
            if grid[temploc]=="#":
                continue
            else:
                while temploc != loc:
                    grid[temploc] = grid[(temploc[0]-dirs[ins][0], temploc[1]-dirs[ins][1])]
                    temploc = (temploc[0]-dirs[ins][0], temploc[1]-dirs[ins][1])
                grid[loc] = '.'
                loc = (loc[0]+dirs[ins][0], loc[1]+dirs[ins][1])
total=0
for loc, val in grid.items():
    if val == "O":
        print(loc)
        total += 100*loc[1]+loc[0]
print(total)