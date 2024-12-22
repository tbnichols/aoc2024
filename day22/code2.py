f =open('input.txt', 'r')
# f = open('sample.txt', 'r')
from collections import defaultdict

bc = defaultdict(int)
total =0
mc = 16777216
for x in f:
    visited = set()
    secret = int(x.strip())
    changes = []
    for i in range (2000):
        prevsec = secret
        secret = ((secret << 6 )^ secret) % mc
        secret = ((secret >> 5) ^ secret)%mc 
        secret = ((secret << 11 )^ secret) % mc
        diff = (prevsec%10)-(secret%10)
        if len(changes) ==4:
            changes.pop(0)
        changes.append(diff)
        if len(changes) ==4:
            if tuple(changes) not in visited:
                bc[tuple(changes)] += secret%10
                visited.add(tuple(changes))

print(total) 
print(max(bc.values()))