f =open('input.txt', 'r')
# f = open('sample.txt', 'r')
CACHE = {}

def tRecur(opts, seeking):
    if seeking in CACHE:
        return CACHE[seeking]
    if len(seeking) ==0:
        return True
    for opt in opts:
        if len(seeking)>=len(opt) and seeking[:len(opt)]==opt:
            if tRecur(opts, seeking[len(opt):]):
                CACHE[seeking]=True
                return True
    CACHE[seeking]=False
    return False

total = 0
options = [x.strip() for x in f.readline().split(",")]

_ = f.readline()
x = f.readline()
while x:
    if tRecur(options, x.strip()):
        total+=1
    x=f.readline()
print(total)