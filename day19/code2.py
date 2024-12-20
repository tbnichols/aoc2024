f =open('input.txt', 'r')
# f = open('sample.txt', 'r')
CACHE = {}

def tRecur(opts, seeking):
    if seeking in CACHE:
        return CACHE[seeking]
    if len(seeking) ==0:
        return 1
    subtot = 0
    for opt in opts:
        if len(seeking)>=len(opt) and seeking[:len(opt)]==opt:
            subtot += tRecur(opts, seeking[len(opt):])
    CACHE[seeking]=subtot
    return subtot

total = 0
options = [x.strip() for x in f.readline().split(",")]

_ = f.readline()
x = f.readline()
while x:
    total+= tRecur(options, x.strip())
    x=f.readline()
print(total)