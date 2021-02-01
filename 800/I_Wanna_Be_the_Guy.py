import sys
steps=sys.stdin.readline().strip()
x=sys.stdin.readline().strip().split()
y=sys.stdin.readline().strip().split()
levels=x[1:]+y[1:]
z=0
for i in range(1,int(steps)+1):
	if str(i) in levels:
		z+=1
if z==int(steps):
	print('I become the guy.')
else:
	print('Oh, my keyboard!')
