import sys
n=int(sys.stdin.readline().strip())
f=sys.stdin.readline().strip().split(' ')
o=[0]*n
for i in range(1,n+1):
	o[int(f[i-1])-1]=str(i)
print(' '.join(o))
