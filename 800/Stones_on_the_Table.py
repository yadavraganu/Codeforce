import sys
n=int(sys.stdin.readline().strip())
table=sys.stdin.readline().strip()
j=0
for i in range(n-1):
	if table[i]==table[i+1]:
		j=j+1
print(j)		
