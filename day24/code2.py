f =open('input.txt', 'r')
# f = open('sample2.txt', 'r')
from collections import defaultdict

gates = {
    "OR": lambda x,y: x|y,
    "XOR": lambda x,y: x^y,
    "AND": lambda x,y: x&y
}
mapping = False
rgso = defaultdict(int)
ops = []
bitshift = 30
for n in f:
    r1, op, r2, _, dest = n.strip().split(" ")

    if r1[0] in ["x","y","z"]:
        if int(r1[1:]) >=bitshift:
            r1 = f"{r1[0]}{(int(r1[1:])-bitshift):02}"
        else:
            for i in [r1, r2,dest]:
                if i[0] not in ["x","y","z"]:
                    rgso[i] = 0
            continue
    if r2[0] in ["x","y","z"]:
        if int(r2[1:]) >=bitshift:
            r2 = f"{r2[0]}{(int(r2[1:])-bitshift):02}"
        else:
            for i in [r1, r2,dest]:
                if i[0] not in ["x","y","z"]:
                    rgso[i] = 0
            continue
    if dest[0] in ["x","y","z"]:
        if int(dest[1:]) >=bitshift :
            dest = f"{dest[0]}{(int(dest[1:])-bitshift):02}"
        else:
            for i in [r1, r2,dest]:
                if i[0] not in ["x","y","z"]:
                    rgso[i] = 0
            continue
    print(f"{r1},{r2},{op},{dest}")
    ops.append((r1,r2,op,dest))
opsorig = ops[:]
x=0
y=0
counter = 1
while True:
    ops = opsorig[:]
    rgs = rgso.copy()
    xs = bin(x)[2:]
    ys = bin(y)[2:]
    for i, c in enumerate(xs):
        rgs[f"x{(len(xs)-1-i):02}"]=int(c)
    for i,c in enumerate(ys):
        rgs[f"y{(len(ys)-1-i):02}"]=int(c)
    
    while len(list(filter(lambda z: z[0] =='z', rgs.keys())))<46-bitshift:
        foplen = len(ops)
        for r1,r2,op,dest in ops[:]:
            if (r1 in rgs or r1[0] in ["x", "y"])and (r2 in rgs or r2[0] in ["x","y"]):
                rgs[dest]=gates[op](rgs[r1],rgs[r2])
                ops.remove((r1,r2,op,dest))
        oplen = len(ops)
        if foplen ==oplen:
            print(rgs)
            print(ops)
            print(list(filter(lambda z: z[0] =='z', rgs.keys())))
            input()

    output = ""
    for z in list(filter(lambda x: x[0] == 'z', sorted(list(rgs.keys())))):
        output = str(rgs[z]) + output
    if counter % 10000 ==0:
        print(counter)
    print(f"{x}, {y}, {output}")
    print(output)
    print(int(output,2))
    if x+y!=int(output,2):
        print(f"{x}, {y}, {output}")
        print(output)
        print(int(output,2))
        input()
    if len(ys)==len(xs) and len(list(filter(lambda i: i=="1", ys)))==len(ys):
        x+=1
        y=0
    else:
        y+=1
        counter +=1

