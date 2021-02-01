import sys 
a=sys.stdin.readline().strip().upper()
b=sys.stdin.readline().strip().upper()
if a==b:
	print(0)
elif a>b:
	print(1)
elif a<b:
	print(-1)