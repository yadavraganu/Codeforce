import sys
n=int(sys.stdin.readline().strip())
m=sys.stdin.readline().strip().split(' ')
k='EASY'
for i in range(n):
	if m[i]=='1':
		k='HARD'
		break
print(k)
