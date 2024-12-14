f =open('input.txt', 'r')
# f = open('sample.txt', 'r')
import re
from collections import defaultdict
from functools import reduce
maxx, maxy = [int(ch) for ch in f.readline().strip().split(" ")]
robo = f.readline()
bots = set()

while robo:
    bots.add(tuple([int(x) for x in re.search(r".*=(\d+),(\d+) .+=(-?\d+),(-?\d+).*", robo).groups()]))
    robo = f.readline()

cur = 0
maxcont = 0

while cur<100000:
    newpos = set()
    newpos.update(map(lambda x: ((x[0]+x[2]*cur)%maxx,(x[1]+x[3]*cur)%maxy), bots))
    contgroup = 0
    vandq = set()
    for y in range(maxy):
        row = ""
        for x in range(maxx):
            if (x,y) in newpos:
                if (x,y) not in vandq:
                    conts = set([(x,y)])
                    queue = [(x,y)]
                    while len(queue) !=0:
                        ele = queue.pop()
                        a,b = ele
                        for cand in [(a,b-1),(a,b+1),(a+1,b),(a-1,b)]:
                            if cand in newpos:
                                if cand not in vandq:
                                    vandq.add(cand)
                                    conts.add(cand)
                                    queue.append(cand)
                    contgroup = max(contgroup, len(conts))
                row+="X"
            else:
                row+="."
        print(row)

    print(cur)
    if contgroup>maxcont:
        maxcont = contgroup
        input()
    cur+=1