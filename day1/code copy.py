from collections import defaultdict
f =open('input.txt', 'r')
ll = defaultdict(int)
rl = defaultdict(int)
for x in f:
	l, r = list(map(lambda y: int(y.strip()), filter(lambda z: z!= '', x.strip().split(" "))))
	ll[l]+=1
	rl[r]+=1
total = 0
for i in ll:
	total += ll[i] * i * rl[i] 
print(total)	
