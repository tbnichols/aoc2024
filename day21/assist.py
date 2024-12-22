from bidict import bidict
inp = "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"

dirgoals = bidict({'^': (0,1), "A": (0,2), '<': (1,0), 'v':(1,1), '>':(1,2)})
commands = {"<": (0,-1),"^": (-1,0), ">": (0,1),"v": (1,0)}
def compress(i):
    start = dirgoals["A"]
    comped=""
    for ch in i:
        if ch in commands:
            start = (start[0]+commands[ch][0], start[1]+commands[ch][1])
        else:
            comped+= dirgoals.inverse[start]
    return comped

comp1 = compress(inp)
comp2 = compress(comp1)
print(comp1)
print(comp2)