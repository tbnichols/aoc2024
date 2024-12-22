f =open('input.txt', 'r')
# f = open('sample.txt', 'r')


total =0
mc = 16777216
for x in f:
    secret = int(x.strip())
    for i in range (2000):
        secret = ((secret << 6 )^ secret) % mc
        secret = ((secret >> 5) ^ secret)%mc 
        secret = ((secret << 11 )^ secret) % mc
    total+=secret
    print(secret)

print(total) 