f =open('input.txt', 'r')
# f = open('sample.txt', 'r')

total = 0
line = f.read().strip()
left = 0
inc = True
right = len(line)-1
if right %2 ==1:
	right = right-1
remaining = int(line[right])
index = 0
while left < right:
	if left %2 == 0:
		for i in range(int(line[left])):
			print(f" {index} * {left//2}")
			total += (index * left //2)
			index +=1
		left+=1
		inc = True
	else:
		slots = int(line[left])
		while slots>0:
			if remaining > 0:
				total += (index * right //2)
				print(f" {index} * {right//2}")
				index+=1
				remaining-=1
				slots-=1
			if remaining == 0:
				right -=2
				inc = False
				if right>left:
					remaining = int(line[right])
		left +=1
while remaining>0:
	total += (index*right//2)
	index+=1
	remaining-=1
print(total)
print(inc)