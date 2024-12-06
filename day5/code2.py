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
		
		valid = False
		changed = False
		while not valid:
			valid = True
			for e in range(len(line)):
				if valid and line[e] in rules:
					for t in range(e):
						if line[t] in rules[line[e]]:
							temp = line[t]
							line[t]=line[e]
							line[e] = temp
							valid = False
							changed = True
							break
		if changed:
			# print(line)
			total += line[len(line)//2]


print(total)	
