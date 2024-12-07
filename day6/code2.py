# f =open('sample.txt', 'r')
f =open('input.txt', 'r')
visited = set()
ops = set()
grid = []
for x in f:
	grid.append(list(x.strip()))
loc = (0,0)
start = (0,0)
direction = (-1,0)
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == '^':
			loc = (i,j)
			start = loc
			visited.add(loc)
			grid[i][j]=tuple([direction])
rotation = {(0,1):(1,0), (1,0): (0,-1), (0,-1): (-1,0), (-1,0):(0,1)}

# def isEscapeable(grid, loc, direction):
# 	prevDirection = direction
# 	while rotation[prevDirection] != direction:
# 		prevDirection = rotation[prevDirection]
# 	clonegrid=[]
# 	for i in grid:
# 		clonegrid.append(i[:])
# 	clonegrid[loc[0]+prevDirection[0]][loc[1]+prevDirection[1]]='#'
# 	while 0<=loc[0]<len(clonegrid) and 0<=loc[1]<len(clonegrid[0]):
# 		# print(loc)
# 		if not (0<=loc[0]+direction[0]<len(clonegrid) and 0<=loc[1]+direction[1]<len(clonegrid[0])):
# 			break
# 		if clonegrid[loc[0]+direction[0]][loc[1]+direction[1]] =='#':
# 			direction = rotation[direction]
# 		else:
# 			loc = (loc[0]+direction[0],loc[1]+direction[1])
# 			if isinstance(clonegrid[loc[0]][loc[1]], tuple) and direction in clonegrid[loc[0]][loc[1]]:
# 				return False
# 			if isinstance(clonegrid[loc[0]][loc[1]], str) :
# 				clonegrid[loc[0]][loc[1]] = tuple([direction])
# 			else: 
# 				clonegrid[loc[0]][loc[1]] = tuple(list(clonegrid[loc[0]][loc[1]])+[direction])
# 	return True

	

while 0<=loc[0]<len(grid) and 0<=loc[1]<len(grid[0]):
	# print(loc)
	if not (0<=loc[0]+direction[0]<len(grid) and 0<=loc[1]+direction[1]<len(grid[0])):
		break
	if grid[loc[0]+direction[0]][loc[1]+direction[1]] =='#':
		direction = rotation[direction]
	else:
		# if not isEscapeable(grid, loc, rotation[direction]):
		# 	ops.add((loc[0]+direction[0],loc[1]+direction[1]))
		loc = (loc[0]+direction[0],loc[1]+direction[1])
		visited.add(loc)
		# if isinstance(grid[loc[0]][loc[1]], str) :
		# 	grid[loc[0]][loc[1]] = tuple([direction])
		# else: 
		# 	grid[loc[0]][loc[1]] = tuple(list(grid[loc[0]][loc[1]])+[direction])

# h = open("travout.txt", 'w')
# for i in grid:
	# h.write(i+'\n')
print(len(visited))	
# print(ops)
visited.discard(start)

for i in visited:
	loc = start
	direction = (-1,0)
	clonegrid=[]
	clonevisit=set()
	for j in grid:
		clonegrid.append(j[:])
	clonevisit.add((start, direction))
	clonegrid[i[0]][i[1]] = '#'
	while 0<=loc[0]<len(clonegrid) and 0<=loc[1]<len(clonegrid[0]):
		# print(loc)
		if not (0<=loc[0]+direction[0]<len(clonegrid) and 0<=loc[1]+direction[1]<len(clonegrid[0])):
			break
		if clonegrid[loc[0]+direction[0]][loc[1]+direction[1]] =='#':
			direction = rotation[direction]
		else:
			loc = (loc[0]+direction[0],loc[1]+direction[1])
			if (loc, direction) in clonevisit:
				ops.add(i)
				break
			# if isiVnstance(clonegrid[loc[0]][loc[1]], str) :
			# 	clonegrid[loc[0]][loc[1]] = tuple([direction])
			# else: 
			# 	clonegrid[loc[0]][loc[1]] = tuple(list(clonegrid[loc[0]][loc[1]])+[direction])
			clonevisit.add((loc, direction))

print(len(ops))