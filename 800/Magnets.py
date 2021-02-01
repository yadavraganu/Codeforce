import sys
n=int(sys.stdin.readline().strip())
if n==1:
	k=1
	for i in range(n):
		m=sys.stdin.readline().strip()
else:
	k=0
	prev=''
	for i in range(n):
		m=sys.stdin.readline().strip()
		if m!=prev:
			k+=1
			prev=m
print(k)
