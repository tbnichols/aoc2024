f =open('input.txt', 'r')
# f = open('sample.txt', 'r')
total = 0
for x in f:
	goal, eles = x.strip().split(":")
	goal = int(goal.strip())
	eles = list(map(lambda x: x.strip(), eles.strip().split(" ")))
	tracker = 0
	while tracker < 3**(len(eles)-1):
		running = eles[0]
		for i,elem in enumerate(eles[1:]):
			# print(running)
			if (tracker // (3**(i)))%3 == 1:
				# print(str(running) + "*" + elem)
				running = int(running)*int(elem)
				# print(running)
				# input()
			elif(tracker // (3**(i)))%3 == 2:
				# print(str(running) + "+" + elem)
				running =int(running)+int(elem)
				# print(running)
				# input()
			else:
				# print(str(running) + "||" + elem)
				running = str(running) + elem
				# print(running)
				# input()
		# print(running)
		if int(running) == goal:
			total += goal
			break
		tracker +=1
print(total)