import sys
n1=sys.stdin.readline().strip()
n2=sys.stdin.readline().strip()
n3=''
for i in range(int(len(n1))):
	if int(n1[i])+int(n2[i]) in [1]:
		n3=n3+'1'
	else:
		n3=n3+'0'
print (n3)
