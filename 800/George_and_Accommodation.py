import sys
n=int(sys.stdin.readline().strip())
o=0
for i in range(n):
	t=sys.stdin.readline().strip().split(' ')
	p,q=int(t[0]),int(t[1])
	if q-p>=2:
		o+=1
print(o)
