inp=list(map(int,(input().split())))
def isPrime(n):
    for j in range(2,n):
        if n%j==0 and n!=2:
            return False 
    return True
primelist=[p for p in range(2,inp[0]+1) if isPrime(p)]
s=0
for i in range(0,len(primelist)-1):
    if primelist[i]+primelist[i+1]+1 in primelist:
        s+=1
if s>=inp[1]:
    print('YES')
else:
    print('NO')            