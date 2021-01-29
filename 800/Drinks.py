import sys
n=int(sys.stdin.readline().strip())
d=sys.stdin.readline().strip().split(' ')
o=0
for i in range(n):
	o=o+int(d[i])
print(o/n)
