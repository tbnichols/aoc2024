f =open('input.txt', 'r')
# f = open('sample.txt', 'r')
import re
from collections import defaultdict
from functools import reduce
maxx, maxy = [int(ch) for ch in f.readline().strip().split(" ")]
robo = f.readline()
quads = defaultdict(int)

def quadck(pos, dim):
    if pos <(dim//2):
        return 0
    if pos>(dim//2):
        return 1
    return 2

while robo:
    xpos, ypos, xvel, yvel = [int(x) for x in re.search(r".*=(\d+),(\d+) .+=(-?\d+),(-?\d+).*", robo).groups()]
    # print(f"{xpos}, {ypos}, {xvel}, {yvel}")
    xposfinal = xpos +100*xvel
    yposfinal = ypos +100*yvel
    quads[(quadck(xposfinal%maxx, maxx), quadck(yposfinal%maxy, maxy))] +=1
    robo = f.readline()
print(quads)

print(reduce(lambda x,y: x*y, [quads[i] for i in quads.keys() if i[0]<2 and i[1]<2]))