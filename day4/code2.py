from functools import reduce
f =open('input.txt', 'r')
total = 0
search = []
directions = [(1,1), (1,-1), (-1,1), (-1,-1)]
for x in f:
	search.append(x.strip())
for i in range(len(search)):
	for j in range(len(search[0])):
		if search[i][j] =='A':
			if 0<=(i-1) and (i+1)<len(search) and 0<=(j-1) and (j+1)<len(search[0]):
				mOcc = list(filter(lambda x: search[i+x[1]][j+x[0]] == 'M', directions))
				sOcc = list(filter(lambda x: search[i+x[1]][j+x[0]] == 'S', directions))
				if len(mOcc) == len(sOcc) == 2 and search[i-1][j-1] != search[i+1][j+1]:
					total+=1
print(total)	
