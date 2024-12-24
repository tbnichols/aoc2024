f =open('input.txt', 'r')
# f = open('sample2.txt', 'r')
# from collections import defaultdict

gates = {
    "OR": lambda x,y: x|y,
    "XOR": lambda x,y: x^y,
    "AND": lambda x,y: x&y
}
mapping = False
rgs = {}
ops = []
n = f.readline().strip()
while True:
    if not mapping and n!='':
        reg, val = list(map(lambda x: x.strip(), n.split(":")))
        rgs[reg]=int(val)
    elif not mapping and n=='':
        mapping= True
    else:
        r1, op, r2, _, dest = n.split(" ")
        ops.append((r1,r2,op,dest))
    n=f.readline().strip()
    if mapping and n=="":
        break

while len(ops)!=0:
    for r1,r2,op,dest in ops[:]:
        if r1 in rgs and r2 in rgs:
            rgs[dest]=gates[op](rgs[r1],rgs[r2])
            ops.remove((r1,r2,op,dest))

output = ""
for z in list(filter(lambda x: x[0] == 'z', sorted(list(rgs.keys())))):
    output = str(rgs[z]) + output
print(output)
print(int(output,2))

