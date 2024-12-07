f =open('input.txt', 'r')
visited = set()
grid = []
for x in f:
	grid.append(x.strip())
loc = (0,0)
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == '^':
			loc = (i,j)
			visited.add(loc)
direction = (-1,0)
rotation = {(0,1):(1,0), (1,0): (0,-1), (0,-1): (-1,0), (-1,0):(0,1)}
g = open("gridout.txt", 'w')
for i in grid:
	g.write(i+'\n')

while 0<=loc[0]<len(grid) and 0<=loc[1]<len(grid[0]):
	# print(loc)
	try:
		if not (0<=loc[0]+direction[0]<len(grid) and 0<=loc[1]+direction[1]<len(grid[0])):
			break
		if grid[loc[0]+direction[0]][loc[1]+direction[1]] =='#':
			direction = rotation[direction]
		else:
			loc = (loc[0]+direction[0],loc[1]+direction[1])
			visited.add(loc)
			if grid[loc[0]][loc[1]]!='^':
				grid[loc[0]] = grid[loc[0]][:loc[1]]+'X'+grid[loc[0]][loc[1]+1:]
	except:
		break

h = open("travout.txt", 'w')
for i in grid:
	h.write(i+'\n')
print(len(visited))	
