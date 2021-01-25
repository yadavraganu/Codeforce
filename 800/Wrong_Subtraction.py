import sys
i=sys.stdin.readline().strip().split(' ')
k,n=int(i[0]),int(i[1])
for i in range(n):
	if k%10==0:
		k=k//10
	else:
		k=k-1
print("{:.0f}".format(k))	