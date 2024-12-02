f =open('sample.txt', 'r')
safe = 0
for x in f:
    numlist = list(map(int, x.strip().split(" ")))
    for j in range(len(numlist)):
        nums = numlist[:]
        nums.pop(j)
        prev = nums[0]-nums[1]
        if abs(prev) == 0 or abs(prev)>3:
            continue
        tempSafe = True
        for i in range(len(nums)-2):
            cur = nums[i+1]-nums[i+2]
            if (prev < 0 and cur >=0) or (prev > 0 and cur <= 0):
                tempSafe = False
                break
            if abs(cur) == 0 or abs(cur)>3:
                tempSafe = False
                break
            else:
                prev = cur
        if tempSafe:
            safe+=1
            break

print(safe)	

