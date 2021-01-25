import sys
x=y=0 
for i in range(1,6):
    b=sys.stdin.readline().strip().split(' ')
    for j in range(1,len(b)+1):
        if int(b[j-1])==1:
            x=i
            y=j
print(abs(x-3)+abs(y-3))