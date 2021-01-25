import sys
a=sys.stdin.readline().strip().split(' ')
n,t=int(a[0]),int(a[1])
b=sys.stdin.readline().strip()
line=list(b)
while t>=1:
    i=0
    while i<=n-2:
        if line[i]=='B' and line[i+1]=='G':
            line[i],line[i+1]=line[i+1],line[i]
            i+=2
        else:
            i+=1
        if i>n-1:
            break

    t-=1
print(''.join(line))
