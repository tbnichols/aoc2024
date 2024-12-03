from functools import reduce
f =open('input.txt', 'r')
total = 0
flag = True
for x in f:
	pots = x.strip().split("mul")
	for pot in pots:
		if flag and pot.find("(") == 0 and 4<=pot.find(")")<=8:
			test = pot[pot.find("(")+1:pot.find(")")]
			if reduce(lambda x,y: x&y, map(lambda z: z.isdigit() or z == ',', test)):
				l, r = list(map(int, test.split(",")))
				total += l*r
		if flag and pot.find("don't()")!=-1 and pot.rfind("do()")<pot.rfind("don't()"):
			flag = False
		elif not flag and pot.find("do()")!=-1 and pot.rfind("don't()") < pot.rfind("do()"):
			flag = True
			
print(total)	
