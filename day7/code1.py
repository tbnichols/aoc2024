f =open('input.txt', 'r')
# f = open('sample.txt', 'r')
total = 0
for x in f:
	goal, eles = x.strip().split(":")
	goal = int(goal.strip())
	eles = list(map(lambda x: x.strip(), eles.strip().split(" ")))
	tracker = 0
	while tracker < 2**(len(eles)-1):
		teststr = "("*(len(eles))
		for i,elem in enumerate(eles[:-1]):
			# print(teststr)
			teststr = teststr + " " + str( elem) + ") "
			if (tracker // (2**i))%2 == 1:
				teststr = teststr +  "*"
			else:
				teststr = teststr + "+"
		teststr = teststr +  " " + eles[-1] +")"
		# print(teststr)
		# print(eval(teststr))
		if eval(teststr) == goal:
			total += goal
			break
		tracker +=1
print(total)