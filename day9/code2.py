f =open('input.txt', 'r')
# f = open('sample.txt', 'r')

total = 0
line = list(map(lambda x: [int(x),int(x)], f.read().strip()))
left = 0
inc = True
right = len(line)-1
if right %2 ==1:
	right = right-1
index = 0
while right > 0:
	index = line[0][0]
	left = 1
	while left < right:
		# print(f"{line[left]}, {line[right]}")
		if line[left][0]>=line[right][0]:
			index+= line[left][1]-line[left][0]
			for i in range(line[right][0]):
				# print(f" {index} * {right//2}")
				total += (index * right // 2)
				index +=1
				line[left][0]-=1
				line[right] = 'x'
			break
		else:
			index += line[left][1] + line[left+1][1]
			left +=2
	if line[right]!='x':
		index -= line[left-1][1]
		for i in range(line[right][0]):
			# print(f" {index} * {right//2}")
			total += (index * right//2)
			index +=1
	right -=2
print(total)