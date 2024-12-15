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
            if val != 'O':
                grid[(curx*2,cury)] = val
                grid[(curx*2+1,cury)] = val
            elif val =="O":
                grid[(curx*2,cury)] = '['
                grid[(curx*2+1,cury)] = ']'
            if val == '@':
                loc = (curx*2, cury)
                grid[(curx*2+1, cury)] = '.'
        cury+=1
    else:
        for ins in x.strip():
            temploc = loc
            if ins in ["<", ">"]:
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
            else:
                tomove = [loc]
                hit = False
                disps = [temploc]
                dist = 0
                while hit == False and len(disps) !=0:
                    newdisps = []
                    for disp in disps:
                        if grid[(disp[0]+dirs[ins][0], disp[1]+dirs[ins][1])]==']': ## hit something, can't move further
                            disps.append((disp[0]+dirs[ins][0], disp[1]+dirs[ins][1]))
                            disps.append((disp[0]+dirs[ins][0]-1, disp[1]+dirs[ins][1]))
                            tomove.append((disp[0]+dirs[ins][0], disp[1]+dirs[ins][1]))
                            tomove.append((disp[0]+dirs[ins][0]-1, disp[1]+dirs[ins][1]))
                        if grid[(disp[0]+dirs[ins][0], disp[1]+dirs[ins][1])]=='[': ## hit something, can't move further
                            disps.append((disp[0]+dirs[ins][0], disp[1]+dirs[ins][1]))
                            disps.append((disp[0]+dirs[ins][0]+1, disp[1]+dirs[ins][1]))
                            tomove.append((disp[0]+dirs[ins][0], disp[1]+dirs[ins][1]))
                            tomove.append((disp[0]+dirs[ins][0]+1, disp[1]+dirs[ins][1]))
                        if grid[(disp[0]+dirs[ins][0], disp[1]+dirs[ins][1])]=='#': ## hit something, can't move further
                            hit = True
                    disps = newdisps
                if hit:
                    continue
                else:
                    moved = set()
                    for moving in tomove[::-1]:
                        if moving in moved:
                            continue
                        grid[(moving[0]+dirs[ins][0], moving[1]+dirs[ins][1])] = grid[moving]
                        grid[moving] = '.'
                        moved.add(moving)
                    loc = (loc[0]+dirs[ins][0], loc[1]+dirs[ins][1])
total=0
for loc, val in grid.items():
    if val == "[":
        print(loc)
        total += 100*loc[1]+loc[0]
print(total)