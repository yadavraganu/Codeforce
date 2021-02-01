import sys
n=sys.stdin.readline().strip()
curr=0
max1=0
for j in range(int(n)):
	i=sys.stdin.readline().strip().split(' ')
	k,n=int(i[0]),int(i[1])
	curr=curr-k+n
	if max1<curr:
		max1=curr
print(max1)		