import sys 
a=sys.stdin.readline().strip()
n,t=int(a[0]),int(a[1])
b=sys.stdin.readline().strip()
q=''
for i in range(len(b)-1):
    if b[i]=='B' and  b[i]=='G':
        