f =open('input.txt', 'r')
ll = []
rl = []
for x in f:
	l, r = list(map(lambda y: int(y.strip()), filter(lambda z: z!= '', x.strip().split(" "))))
	ll.append(l)
	rl.append(r)
ll.sort()
rl.sort()
total = 0
for i in range(len(ll)):
	total += abs(rl[i]-ll[i])
print(total)	
