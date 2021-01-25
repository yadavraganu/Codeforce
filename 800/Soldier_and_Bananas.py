import sys
i=sys.stdin.readline().strip().split(' ')
k,n,w=int(i[0]),int(i[1]),int(i[2])
cost=0
for j in range(1,w+1):
    cost=cost+j*k
if cost>n:
    print(cost-n)
else:
    print(0)