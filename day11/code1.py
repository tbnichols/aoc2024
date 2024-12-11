f =open('input.txt', 'r')
#f = open('sample.txt', 'r')
from collections import defaultdict
stones = defaultdict(int)
for x in f.read().strip().split(' '):
    stones[int(x)]+=1
for i in range(75):
    nextstones = defaultdict(int)
    for stone in stones:
        st =str(stone)
        if stone == 0:
            nextstones[1]+=stones[0]
        elif len(st)%2==0:
            stone1 = int(st[:(len(st)//2)])
            stone2 = int(st[(len(st)//2):])
            nextstones[stone1]+=stones[stone]
            nextstones[stone2]+=stones[stone]
        else:
            nextstones[stone*2024]+=stones[stone]
    stones=nextstones
    print(stones)
total=0
for i in stones.values():
   total+=i 
print(total)
