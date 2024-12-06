from collections import defaultdict
f =open('input.txt', 'r')
total = 0
rules = defaultdict(set)
parsing = True
for x in f:
	if parsing and x.strip()!="":
		k,v = x.strip().split("|")
		rules[int(k)].add(int(v))
	elif parsing:
		parsing = False
	else:
		line = list(map(int, x.strip().split(',')))
		valid = True
		for e in range(len(line)):
			if line[e] in rules:
				for t in line[:e]:
					if t in rules[line[e]]:
						valid = False
						break
		if valid:
			total += line[len(line)//2]


print(total)	
