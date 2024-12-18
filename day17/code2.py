f =open('input.txt', 'r')
# f = open('sample.txt', 'r')

bord = ["000", "001", "010", "011", "100", "101", "110", "111"]
regA = int(f.readline().split(":")[1].strip())
regB = int(f.readline().split(":")[1].strip())
regC = int(f.readline().split(":")[1].strip())
f.readline()
ins = [int(i) for i in f.readline().strip().split(':')[1].strip().split(',')]
print(ins[::-1])
out=[]
numpots = ["0000000000"]
for i in ins[::-1]:
    tempnums = []
    for num in numpots:
        for bpot in bord:
            potnum = num+bpot
            # print(num)
            # print(bpot)
            C = int(potnum[len(potnum)-(int(bpot,2)^5)-3:len(potnum)-(int(bpot,2)^5)], 2)
            if int(bpot,2)^5^6^C == i:
                tempnums.append(potnum)
                calcans = int(bpot,2)^5^6^C
                print(f"goal: {i}, C: {C}, B: {bpot}, ans: {calcans}")
    numpots = tempnums
    print(numpots)
    print([int(cand, 2) for cand in numpots])
    input()
print(numpots)
print([int(num,2) for num in numpots])
print(min([int(num,2) for num in numpots]))