import sys
i=sys.stdin.readline().strip().split(' ')
k,n=int(i[0]),int(i[1])
j=0
while True:
	j=j+1
	k=k*3
	n=n*2
	if k>n:
		print(j)
		break
	