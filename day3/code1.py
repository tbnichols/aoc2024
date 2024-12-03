from functools import reduce
f =open('input.txt', 'r')
total = 0
for x in f:
	pots = x.strip().split("mul")
	for pot in pots:
		if pot.find("(") == 0 and 4<=pot.find(")")<=8:
			test = pot[pot.find("(")+1:pot.find(")")]
			if reduce(lambda x,y: x&y, map(lambda z: z.isdigit() or z == ',', test)):
				l, r = list(map(int, test.split(",")))
				total += l*r
print(total)	
