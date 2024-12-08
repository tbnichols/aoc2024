f =open('input.txt', 'r')
from collections import defaultdict
# f = open('sample.txt', 'r')
antis = set()
freqs = set()
grid = []
for x in f:
	grid.append(list(x.strip()))
	freqs.update(list(x.strip()))

freq_locs = defaultdict(set)
for i, row in enumerate(grid):
	for j, el in enumerate(row):
		if el != '.':
			freq_locs[el].add((i,j))

def check(i,j, values):
	diff_list = map(lambda y: map(lambda x: (x[0]-i, x[1]-j) ,y), values)
	for mults in diff_list:
		multlist = list(mults)
		for val1 in multlist:
			for val2 in multlist:
				try:
					if val1 == (0,0) or val2 == (0,0) or (val1!=val2 and val1[0]/val2[0] == val1[1]/val2[1]):
						return True
				except:
					pass
	return False


for i in range(len(grid)):
	for j in range(len(grid[0])):
		if check(i,j, freq_locs.values()):
			antis.add((i,j))

for anti in antis:
	grid[anti[0]][anti[1]] = '#'
print(len(antis))
# print(grid)
g = open("gridout.txt", 'w')
for i in grid:
	g.write("".join(i)+'\n')

