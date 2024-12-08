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
for loc_set in freq_locs.values():
	for x in loc_set:
		for y in loc_set:
			if x != y:
				diff = (x[0]-y[0], x[1]-y[1])
				anti_loc = (x[0]+diff[0], x[1]+diff[1])
				try:
					if 0<=anti_loc[0]<len(grid) and 0<=anti_loc[1]<len(grid[anti_loc[0]]):
						if anti_loc == (11,9):
							print(x)
							print(y)
						antis.add(anti_loc)
				except:
					pass


print(len(grid))
for anti in antis:
	grid[anti[0]][anti[1]] = '#'
print(len(antis))
print(antis)
# print(grid)
g = open("gridout.txt", 'w')
for i in grid:
	g.write("".join(i)+'\n')

