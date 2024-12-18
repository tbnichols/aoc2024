f =open('input.txt', 'r')
# f = open('sample.txt', 'r')

regA = int(f.readline().split(":")[1].strip())
regB = int(f.readline().split(":")[1].strip())
regC = int(f.readline().split(":")[1].strip())
f.readline()
ins = [int(i) for i in f.readline().strip().split(':')[1].strip().split(',')]
opers = [0,1,2,3, regA, regB, regC, 7]
pointer = 0
out=[]
while pointer < len(ins):
    op = ins[pointer]
    oper = opers[ins[pointer+1]]
    print(f"{op},{ins[pointer+1]}, {oper}, {opers}, {pointer}, {opers[5]%8}, {opers[6]%8}")
    match op:
        case 0:
            opers[4] = opers[4]//(2**oper)
        case 1:
            opers[5] = opers[5]^ins[pointer+1]
        case 2:
            opers[5] = oper%8
        case 3:
            if opers[4] ==0:
                pass
            else:
                pointer = ins[pointer+1]
                continue
        case 4:
            opers[5] = opers[5]^opers[6]
        case 5:
            out.append(str(oper%8))
            print(oper%8)
        case 6:
            opers[5] = opers[4]//(2**oper)
        case 7:
            opers[6] = opers[4]//(2**oper)
    # print(f"{op}, {oper}, {opers}, {pointer}")
    # print(out)
    # input()
    pointer+=2
print(",".join(out)) 