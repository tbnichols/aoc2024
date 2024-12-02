f =open('input.txt', 'r')
safe = 0
for x in f:
    nums = list(map(int, x.strip().split(" ")))
    prev = nums[0]-nums[1]
    if abs(prev) == 0 or abs(prev)>3:
        continue
    for i in range(len(nums)-2):
        cur = nums[i+1]-nums[i+2]
        if (prev < 0 and cur >=0) or (prev > 0 and cur <= 0):
            safe -=1
            break
        if abs(cur) == 0 or abs(cur)>3:
            safe -=1
            break
        else:
            prev = cur
    safe+=1

print(safe)	

