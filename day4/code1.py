f =open('input.txt', 'r')
total = 0
search = []
directions = [(0,1), (1,0), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
for x in f:
	search.append(x.strip())
print(search)
for i in range(len(search)):
	for j in range(len(search[0])):
		if search[i][j] =='X':
			for dir in directions:
				if 0<=(i+dir[0]*3)<len(search) and 0<=(j+dir[1]*3)<len(search[0]) and search[i+dir[0]][j+dir[1]] =='M' and search[i+dir[0]*2][j+dir[1]*2] =='A' and search[i+dir[0]*3][j+dir[1]*3] =='S':
					total+=1
print(total)	
