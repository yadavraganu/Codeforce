import sys
t=sys.stdin.readline().strip().split(' ')
n,h=int(t[0]),int(t[1])
f=sys.stdin.readline().strip().split(' ')
o=n
for i in range(n):
	if int(f[i])>h:
		o+=1
print(o)
