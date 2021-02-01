import sys
n=int(sys.stdin.readline().strip())
a=''
for i in range(1,n+1):
	b='love' if i%2==0 else 'hate'
	if i==n:
		a=a+'I '+b+' it '
	else:
		a=a+'I '+b+' that '
print(a.strip())
